#These next two lines aren't needed unless you're having trouble running kivi.app
#import pip._internal as pip
#pip.main(['install', 'kivy'])

import sys

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
from kivymd.uix.list import MDListItem,MDListItemHeadlineText,MDListItemSupportingText
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import sys
import sys
sys.path.insert(0,'C:/Users/Cameron/Desktop/Capstone/kivy_venv/ExerciseApp_main/CloudAPIs')
import os
_CloudAPIs = os.path.join(os.getcwd(),os.path.dirname("CloundAPIs"))
_libs = os.path.join(os.getcwd(),os.path.dirname("libs"))


from CloudAPIs import sqlInterface 
from CloudAPIs import APIUnitTests 
# sys.path.insert(0,_CloudAPIs)
# sys.path.insert(0,_libs)

# from CloudAPIs.sqlInterface import *
# from CloudAPIs.APIUnitTests import *


x = APIUnitTests.s2_demo_query()
print(x)
for i in range(3):
    print("user: {}".format(x[i][4]))
    print(x[i][2])
    


# sqlInterface.new_user({
#         "AccountNumber" : None,
#         "Username" : 'cam',
#         "Email" : 'clr064@latech.edu',
#         "PhoneNumber" : '456',
#         "Fname" : "cam",
#         "Minit" : "l",
#         "Lname" : 'rob',
#         "UserDoB" : '2011-05-05',
#         "PasswordHash" : 'qwert'})


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
    pass

class SignupScreen(Screen):
    pass

class ForgotPasswordScreen(Screen):
    pass

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
            # print("user: {}".format(x[i][4]))
            # print(x[i][2])
        # self.ml.add_widget(List.TwoLineListItem(
        #     text=msg_to_add,
        #     secondary_text=from_who,
        #     markup=True,
        #     text_size=(self.width, None),
        #     size_hint_y=None,
        #     font_size=self.height / 23,
        #     ))

kv = Builder.load_file('ExerciseAppKivyCode.kv') # This is the existing kv string for the login screen

class ExerciseApp(MDApp):
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
    


if __name__ == "__main__":
    myapp = ExerciseApp()
    myapp.run()
