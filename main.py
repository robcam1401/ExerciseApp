from email import feedparser
#These next two lines aren't needed unless you're having trouble running kivi.app
import pip._internal as pip
pip.main(['install', 'kivy'])
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        label = Label(text="This is the Profile Screen")
        self.add_widget(label)

class FeedScreen(Screen):
    def __init__(self, **kwargs):
        super(FeedScreen, self).__init__(**kwargs)
        label = Label(text="This is the Feed Screen")
        self.add_widget(label)

class ExploreScreen(Screen):
    def __init__(self, **kwargs):
        super(ExploreScreen, self).__init__(**kwargs)
        label = Label(text="This is the Explore Screen")
        self.add_widget(label)

class SocialScreen(Screen):
    def __init__(self, **kwargs):
        super(SocialScreen, self).__init__(**kwargs)
        label = Label(text="This is the Social Screen")
        self.add_widget(label)

class NearYouScreen(Screen):
    def __init__(self, **kwargs):
        super(NearYouScreen, self).__init__(**kwargs)
        label = Label(text="This is the Near You Screen")
        self.add_widget(label)

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

        sm.add_widget(profile_screen)
        sm.add_widget(feed_screen)
        sm.add_widget(explore_screen)
        sm.add_widget(social_screen)
        sm.add_widget(near_you_screen)

        # Create a bottom tab bar with buttons
        tab_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        profile_button = Button(text='Profile', on_press=self.switch_to_profile)
        feed_button = Button(text='Feed', on_press=self.switch_to_feed)
        explore_button = Button(text='Explore', on_press=self.switch_to_explore)
        social_button = Button(text='Social', on_press=self.switch_to_social)
        near_you_button = Button(text='Near You', on_press=self.switch_to_near_you)

        tab_bar.add_widget(profile_button)
        tab_bar.add_widget(feed_button)
        tab_bar.add_widget(explore_button)
        tab_bar.add_widget(social_button)
        tab_bar.add_widget(near_you_button)

        # Create a layout for the entire app
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(sm)
        layout.add_widget(tab_bar)

        return layout

    def switch_to_profile(self, instance):
        self.root.current = 'profile'

    def switch_to_feed(self, instance):
        self.root.current = 'feed'

    def switch_to_explore(self, instance):
        self.root.current = 'explore'

    def switch_to_social(self, instance):
        self.root.current = 'social'

    def switch_to_near_you(self, instance):
        self.root.current = 'near_you'

if __name__ == "__main__":
    ExerciseApp().run()
