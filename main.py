#These next two lines aren't needed unless you're having trouble running kivi.app
#import pip._internal as pip
#pip.main(['install', 'kivy'])

from email import feedparser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy_garden.mapview import MapView
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.tabbedpanel import TabbedPanel
#from signup import send_verification_email, generate_verification_code, sign_up_user

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
                on_press: 
                    root.manager.current = 'feed'
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
                #id: email_input
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
                #id: password_input
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

Profile_kv = '''
<ProfileScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Line:
            rectangle: (self.x + dp(60), self.y + dp(60), self.width - dp(120), self.height - dp(120))
            width: 1
            
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Profile Picture and Bio Section
            BoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)

                Image:
                    source: 'IMG_1633.JPG' 
                    size_hint: None, None
                    size: dp(100), dp(80)
                    allow_stretch: True
                    keep_ratio: True
                    border: 1, 1, 1, 1  # White border around the profile picture
                    # Link to Settings

                Button:
                    text: 'Settings'
                    size_hint_y: None
                    height: dp(30)
                    on_press: root.manager.current = 'profile_settings'   

                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: 'Ilana Tetruashvili'
                        font_name: 'Arial'  # Twitter uses Arial
                        font_size: '24sp'  # Twitter-like font size
                        size_hint_y: None
                        height: self.texture_size[1]

                    Label:
                        text: 'Tennis Player from Israel'
                        font_size: '16sp'  # Twitter-like font size
                        size_hint_y: None
                        height: self.texture_size[1]

            # Tabs Section
            BoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)

                Button:
                    text: 'Resources'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Media'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Likes'
                    size_hint_y: None
                    height: dp(30)
                
                Button:
                    text: 'Book'
                    size_hint_y: None
                    height: dp(30)


'''
ProfileSettings_kv = '''
<ProfileSettingsScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Line:
            rectangle: (self.x + dp(60), self.y + dp(60), self.width - dp(120), self.height - dp(120))
            width: 1
            
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Profile Settings Content Section
            Label:
                text: 'Account Settings'
                font_size: '24sp'
                size_hint_y: None
                height: self.texture_size[1]

            TextInput:
                hint_text: 'Username'
                multiline: False
                size_hint_y: None
                height: dp(30)

            TextInput:
                hint_text: 'Email'
                multiline: False
                size_hint_y: None
                height: dp(30)

            TextInput:
                hint_text: 'Phone Number'
                multiline: False
                size_hint_y: None
                height: dp(30)

            Button:
                text: 'Change Profile Picture'
                size_hint_y: None
                height: dp(30)
                # Add functionality to change profile picture

            TextInput:
                hint_text: 'Change Password'
                multiline: False
                password: True
                size_hint_y: None
                height: dp(30)

            Button:
                text: 'Save Changes'
                size_hint_y: None
                height: dp(30)
                #on_press: root.save_changes()  

            # Link to Profile
            Button:
                text: 'Go Back'
                size_hint_y: None
                height: dp(30)
                on_press: root.manager.current = 'profile'
'''

Feed_kv = '''
<FeedScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Line:
            rectangle: (self.x + dp(60), self.y + dp(60), self.width - dp(120), self.height - dp(120))
            width: 1
            
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Feed Content Section
            ScrollView:
                Label:
                    text: 'Feed content goes here.'
                    font_size: '16sp'
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width - dp(20), None
                    valign: 'top'

            # Tabs Section
            BoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)

                Button:
                    text: 'Recent'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Popular'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Trending'
                    size_hint_y: None
                    height: dp(30)

'''
Explore_kv = '''
<ExploreScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Line:
            rectangle: (self.x + dp(60), self.y + dp(60), self.width - dp(120), self.height - dp(120))
            width: 1
            
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Search Bar
            TextInput:
                id: search_input
                hint_text: 'Search...'
                multiline: False
                size_hint_y: None
                height: dp(30)
                on_text_validate: root.on_search(search_input.text)

            # Search Results Section
            ScrollView:
                Label:
                    id: search_results
                    text: ' '
                    font_size: '16sp'
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width - dp(20), None
                    valign: 'top'

'''

Social_kv = '''
<SocialScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Line:
            rectangle: (self.x + dp(60), self.y + dp(60), self.width - dp(120), self.height - dp(120))
            width: 1
            
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Social Content Section
            ScrollView:
                Label:
                    text: 'Your social content goes here.'
                    font_size: '16sp'
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width - dp(20), None
                    valign: 'top'

            # Tabs Section
            BoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)

                Button:
                    text: 'Friends'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Groups'
                    size_hint_y: None
                    height: dp(30)

                Button:
                    text: 'Messages'
                    size_hint_y: None
                    height: dp(30)

            # Link to Profile
            Button:
                text: 'Profile'
                size_hint_y: None
                height: dp(30)
                on_press: root.manager.current = 'profile'
'''

NearYou_kv = '''
<NearYouScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        

    
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(5)
            padding: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: .7, .7

            # Near You Content Section
            ScrollView:
                Label:
                    text: 'Nearby content goes here.'
                    font_size: '16sp'
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width - dp(20), None
                    valign: 'top'

            # Map or Location Section 
            MapView:
                id: mapview
                lat: 32.5259527
                lon: -92.6436849
                zoom: 25
                size_hint: 1,5


                MapMarker:
                    lat: 50.6394
                    lon: 3.057

                MapMarker
                    lat: -33.867
                    lon: 151.206

            
                

            

'''

class ProfileScreen(Screen):
    pass
        
class FeedScreen(Screen):
    pass

class ExploreScreen(Screen):
    def on_search(self, query):
        if query.lower() == 'lesson':
            # Clear previous search results
            self.ids.search_results.clear_widgets()

            # Display an image and headline for tennis lesson
            image = Image(source='lesson.jpg', size_hint=(None, None), size=(300, 200), allow_stretch=True)
            headline = Label(text='Tennis Lesson', font_size='16sp', size_hint_y=None, height=30)
            
            self.ids.search_results.add_widget(image)
            self.ids.search_results.add_widget(headline)
        else:
            # Display a message for other search queries
            self.ids.search_results.text = f'No results found for "{query}"'

class SocialScreen(Screen):
    pass

class NearYouScreen(Screen):
    pass

class ProfileSettingsScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    #def sign_up(self): 
        #user_email = self.ids.email_input.text
        #user_password = self.ids.password_input.text
         #calling sign-up function from signup.py
         #sign_up_user(user_email, user_password)
    pass

class ForgotPasswordScreen(Screen):
    pass

class ExerciseApp(App):
    def build(self):
        # Create a screen manager without transitions for simplicity
        sm = ScreenManager(transition=NoTransition())

        # Create screens and add them to the screen manager
        profile_screen = ProfileScreen(name='profile')
        feed_screen = FeedScreen(name='feed')
        explore_screen = ExploreScreen(name='explore')
        social_screen = SocialScreen(name='social')
        near_you_screen = NearYouScreen(name='near_you')
        profile_screen = ProfileScreen(name='profile')
        profile_settings = ProfileSettingsScreen(name='profile_settings')

        #this will change the order in which the screens appear (Feed Screen is default)
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password_screen'))
        sm.add_widget(feed_screen)
        sm.add_widget(profile_screen)
        sm.add_widget(explore_screen)
        sm.add_widget(social_screen)
        sm.add_widget(near_you_screen)
        sm.add_widget(profile_settings)



        # Create a bottom tab bar with buttons
        tab_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        profile_button = Button(text='Profile', on_press=lambda x: sm.switch_to(profile_screen))
        feed_button = Button(text='Feed', on_press=lambda x: sm.switch_to(feed_screen))
        explore_button = Button(text='Explore', on_press=lambda x: sm.switch_to(explore_screen))
        social_button = Button(text='Social', on_press=lambda x: sm.switch_to(social_screen))
        near_you_button = Button(text='Near You', on_press=lambda x: sm.switch_to(near_you_screen))

        #this will determine the order of the buttons on the tab-bar
        tab_bar.add_widget(feed_button)
        tab_bar.add_widget(explore_button)
        tab_bar.add_widget(near_you_button)
        tab_bar.add_widget(profile_button)
        tab_bar.add_widget(social_button)

        

        # Create a layout for the entire app
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(sm)
        layout.add_widget(tab_bar)
        
        return layout
    
Builder.load_string(kv) # This is the existing kv string for the login screen
Builder.load_string(signup_kv) # This is the existing kv string for the signUp screen
Builder.load_string(ForgotPassWord_kv)
Builder.load_string(Profile_kv)
Builder.load_string(Feed_kv)
Builder.load_string(Explore_kv)
Builder.load_string(NearYou_kv)
Builder.load_string(Social_kv)
Builder.load_string(ProfileSettings_kv)

if __name__ == "__main__":
    ExerciseApp().run()




