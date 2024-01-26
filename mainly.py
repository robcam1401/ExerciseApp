from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Login Page
kv = '''
<CenteredBoxLayout@BoxLayout>:    #layout for the border around the form
    size_hint: None, None
    width: 550
    height: 700
    padding: 10
    spacing: 10
    
#LoginScreen layout  
<LoginScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        CenteredBoxLayout:
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: (1, 1, 1, 1)  # White color for the border
                Line:
                    rectangle: (self.x, self.y, self.width, self.height)
                    width: 1
            Image:
                source: 'login.jpeg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.7} 
            Label:
                text: 'Fitness & Sports App'
                font_name: 'Cedarville_Cursive/CedarvilleCursive-Regular.ttf'          #Font Style
                font_size: '24sp'
                size_hint_y: None
                height: self.texture_size[1]
            TextInput:
                hint_text: 'Phone number, username, or email'
                size_hint_y: None
                height: 40
                multiline: False
            TextInput:
                hint_text: 'Password'
                password: True
                size_hint_y: None
                height: 40
                multiline: False
            Button:
                text: 'Log in'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'main'  # Adjust this as needed (homepage)
            Label:
                text: 'OR'
                size_hint_y: None
                height: 40
            #button for signUp to redirect to Forgot password page
            Button:
                text: 'Forgot password?'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'forgot_password_screen'   
            Widget:
                size_hint_y: None
                height: 40
            BoxLayout:
                size_hint_y: None
                height: 40
                Label:
                    text: "Don't have an account?"
                #button for signUp to redirect to signup page
                Button:
                    text: 'Sign up'
                    on_press: root.manager.current = 'signup'
'''

#layout for the signup page/screen
signup_kv = '''
<SignupScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            width: 550
            height: 700
            padding: 10
            spacing: 10
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # White border
                Line:
                    rectangle: (self.x, self.y, self.width, self.height)
                    width: 1         
            Image:
                source: 'design.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.7} 
            Label:
                text: 'Fitness & Sports App'
                font_name: 'Cedarville_Cursive/CedarvilleCursive-Regular.ttf'
                font_size: '30sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'center_x': 0.5, 'y': 0.6}
            TextInput:
                hint_text: 'Phone number or Email'
                size_hint_y: None
                height: 40
                multiline: False
            TextInput:
                hint_text: 'Full Name'
                size_hint_y: None
                height: 40
                multiline: False
            TextInput:
                hint_text: 'Username'
                size_hint_y: None
                height: 40
                multiline: False
            TextInput:
                hint_text: 'Password'
                size_hint_y: None
                height: 40
                multiline: False
                password: True
            Button:
                text: 'SignUp'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'login'
'''
#layout for forgot password page/screen
ForgotPassWord_kv = '''
<CenteredBoxLayout@BoxLayout>:
    size_hint: None, None
    width: 550
    height: 700
    padding: 10
    spacing: 10

<ForgotPasswordScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        CenteredBoxLayout:
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: (1, 1, 1, 1)
                Line:
                    rectangle: (self.x, self.y, self.width, self.height)
                    width: 1
            Image:
                source: 'design.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.7} 
            Label:
                text: 'Fitness & Sports App'
                font_name: 'Cedarville_Cursive/CedarvilleCursive-Regular.ttf'
                font_size: '24sp'
                size_hint_y: None
                height: self.texture_size[1]
            TextInput:
                id: email
                hint_text: 'Email'
                size_hint_y: None
                height: 40
                multiline: False
            Button:
                text: 'Send Reset Link'
                size_hint_y: None
                height: 40
                on_release: root.send_reset_link(email.text)
            Widget:
                size_hint_y: None
                height: 40
            Label:
                text: "Remember your password?"
                size_hint_y: None
                height: 40
            Button:
                text: 'Log in'
                size_hint_y: None
                height: 40
                on_press: root.manager.current = 'login'

'''
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class ForgotPasswordScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password_screen'))
        return sm
    
Builder.load_string(kv) # This is the existing kv string for the login screen
Builder.load_string(signup_kv) # This is the existing kv string for the signUp screen
Builder.load_string(ForgotPassWord_kv)   # This is the existing kv string for the Forgot Password screen

if __name__ == '__main__':
    MyApp().run()
