#These next two lines aren't needed unless you're having trouble running kivi.app
#import pip._internal as pip
#pip.main(['install', 'kivy'])
import mysql.connector
import configparser
#regular expression library for validation
import re
import bcrypt
from kivy.uix.popup import Popup
from email import feedparser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy_garden.mapview import MapView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.app import MDApp

from kivymd.uix.list import MDListItem,MDListItemHeadlineText,MDListItemSupportingText
from signup import sign_up_user
from kivy.properties import StringProperty
from forgotpassVeri import initiate_password_reset
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import sys
sys.path.insert(0,'C:/Users/Cameron/Desktop/Capstone/kivy_venv/ExerciseApp_main/CloudAPIs')
import os
_CloudAPIs = os.path.join(os.getcwd(),os.path.dirname("CloundAPIs"))
_libs = os.path.join(os.getcwd(),os.path.dirname("libs"))


from CloudAPIs import sqlInterface 
from CloudAPIs import APIUnitTests 

class ProfileScreen(Screen):
    pass
        
class FeedScreen(Screen):
    pass

class ExploreScreen(Screen):
    pass

class SocialScreen(Screen):
    pass

class NearYouScreen(Screen):
    pass

class ProfileSettingsScreen(Screen):
    pass

class LoginScreen(Screen):
    def connect(self):
        # Retrieves user input
        input_email = self.ids.input_email.text
        input_password = self.ids.input_password.text

        # for establishing database connection
        db_connection = get_db_connection()
        cursor = db_connection.cursor()

        # Parameterized query for safe database interaction
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (input_email,))

        result = cursor.fetchone()

        if result:
        # Verifing the hashed password
            stored_password = result[0].encode('utf-8')  # The hashed password from the database
            valid_password = bcrypt.checkpw(input_password.encode('utf-8'), stored_password)

            if valid_password:
                # Correct credentials; proceeds to log in the user
                self.manager.current = 'profile'  
            else:
                # Invalid password;
                # Show an error message or handle invalid login
                pass
        else:
            # Email not found; 
            # Show an error message or handle invalid login
            pass

        cursor.close()
        db_connection.close()


class SignupScreen(Screen):
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
        
    def on_sign_up(self): 
        print("Signup process initiated....") #debugging line
        user_email = self.ids.email_input.text
        ##user_password = self.ids.password_input.text
        
        #print(f"Email entered: {user_email}, Password entered: {user_password}") #for the input values
        
        if self.validate_email(user_email): #and self.validate_password(user_password):
            sign_up_user(user_email)
            #print("Email and password validation passed.") #checking
            #App.get_running_app().user_email = user_email
            # Here, after validation, calls the signup function.
            #sign_up_user(user_email, user_password)
            # Navigate to verification screen
            self.manager.current = 'verification'
        else: 
            print("Email or password validation failed.") #checking
            self.show_popup("Invalid Email", "Please enter a valid email address.")

        
    def validate_email(self, email):
        # Simple regex for validating an email address
        pattern = r'^[\w\.-]+@gmail\.com$'
        return re.match(pattern, email) is not None

   # def validate_password(self, password):
        # Example: Validate password length; Password length should be 8 or more
        #return len(password) >= 8

class SignupVerificationScreen(Screen):
    def verify_code(self):
        user_code = self.ids.verification_code_input.text  
        user_email = App.get_running_app().user_email
        
        # Assuming you have stored the expected code in memory, e.g., in App.get_running_app().verification_code
        expected_code = str(App.get_running_app().verification_code)
        
        if user_code == expected_code:
            # Verification successful, navigate to the next screen
            self.manager.current = 'feed'  # Example target screen
        else:
            # Verification failed, show error
            self.show_popup("Verification Failed", "The code does not match.")


class ForgotPasswordScreen(Screen):
    def send_reset_email(self):
        email = self.ids.email.text
        if self.validate_email(email):
            try:
                # Call the function from forgotpassVeri.py
                initiate_password_reset(email)
                # Inform the user to check their email
                self.show_popup("Success", "A password reset link has been sent to your email.")
                self.manager.current = 'login'
            except Exception as e:
                print(f"Error sending reset email: {e}")
                self.show_popup("Error", "Failed to send password reset email.")
                #return  # Keep the user on the same screen to try again
            finally:
                # Navigate to login page only after successful email sending
                self.manager.current = 'login'
        else:
            self.show_popup("Invalid email", "The email you entered is not valid.")

    def validate_email(self, email):
        # Simple regex for validating an email address
        pattern = r'^[\w\.-]+@gmail\.com$'
        return re.match(pattern, email) is not None

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(600, 200))
        popup.open()



class FriendsScreen(Screen):
    root = ScrollView(size_hint=(1,None),size=(BoxLayout.width,BoxLayout.height))
    def create_friend(self):
        self.btn = Button(text="button", size_hint_y=None,height=20,on_press=self.press_friend)
        self.ids.grid_friend.add_widget(self.btn)

    def press_friend(self,instance):
        print("friends messages")

class GroupsScreen(Screen):
    root = ScrollView(size_hint=(1,None),size=(BoxLayout.width,BoxLayout.height))
    def create_group(self):
        self.btn = Button(text="button", size_hint_y=None,height=20,on_press=self.press_group)
        self.ids.grid_group.add_widget(self.btn)

    def press_group(self,instance):
        print("group messages")

class MessagesScreen(Screen):
    def update_messeges(self):
        x = APIUnitTests.s2_demo_query()
        print(x)
        for i in range(3):
            self.ids.grid_messages.add_widget(
                MDListItem(
                    MDListItemHeadlineText(text = str(x[i][4])),
                    MDListItemSupportingText(text = x[i][2])
                )
            )

kv = Builder.load_file('ExerciseAppKivyCode.kv') # This is the existing kv string for the login screen

class ExerciseApp(MDApp):
    user_email = StringProperty(None) 
    
    def build(self):
        # Create a screen manager without transitions for simplicity
        self.sm = ScreenManager(transition=WipeTransition())

        # Create screens and add them to the screen manager
        profile_screen = ProfileScreen(name='profile')
        feed_screen = FeedScreen(name='feed')
        explore_screen = ExploreScreen(name='explore')
        social_screen = SocialScreen(name='social')
        near_you_screen = NearYouScreen(name='near_you')
        profile_settings = ProfileSettingsScreen(name='profile_settings')
        friends = FriendsScreen(name='friends')
        groups = GroupsScreen(name='groups')
        messages = MessagesScreen(name='messages')

        #this will change the order in which the screens appear (Feed Screen is default)
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(SignupScreen(name='signup'))
        self.sm.add_widget(SignupVerificationScreen(name= 'verification'))
        self.sm.add_widget(ForgotPasswordScreen(name='forgot_password_screen'))
        self.sm.add_widget(feed_screen)
        self.sm.add_widget(profile_screen)
        self.sm.add_widget(explore_screen)
        self.sm.add_widget(social_screen)
        self.sm.add_widget(near_you_screen)
        self.sm.add_widget(profile_settings)
        self.sm.add_widget(friends)
        self.sm.add_widget(groups)
        self.sm.add_widget(messages)



        # Create a bottom tab bar with buttons
        tab_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        profile_button = Button(text='Profile', on_press=lambda x: self.sm.switch_to(profile_screen))
        feed_button = Button(text='Feed', on_press=lambda x: self.sm.switch_to(feed_screen))
        explore_button = Button(text='Explore', on_press=lambda x: self.sm.switch_to(explore_screen))
        social_button = Button(text='Social', on_press=lambda x: self.sm.switch_to(social_screen))
        near_you_button = Button(text='Near You', on_press=lambda x: self.sm.switch_to(near_you_screen))

        #this will determine the order of the buttons on the tab-bar
        tab_bar.add_widget(feed_button)
        tab_bar.add_widget(explore_button)
        tab_bar.add_widget(near_you_button)
        tab_bar.add_widget(profile_button)
        tab_bar.add_widget(social_button)

        

        # Create a layout for the entire app
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.sm)
        layout.add_widget(tab_bar)
        
        return layout
    
def get_db_connection():
    config= configparser.ConfigParser()
    config.read('config.ini')
    #to connect to database
    db_connection = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['db']
    )
    return db_connection   


if __name__ == "__main__":
    myapp = ExerciseApp()
    myapp.run()
