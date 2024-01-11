from kivy.app import App
from kivy_garden.mapview import MapView
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout

# Login Page
 
# You can create your kv code in the Python file
Builder.load_string("""
<ProfileScreen>:
    Label:
        text: "profile"
    BoxLayout:
        orentation: "horizontal"
        size_hint: (1,0.1)
        Button:
            text: "profile"
                
        Button:
            text: "feed"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'FeedScreen'
        Button:
            text: "explore"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ExploreScreen'
        Button:
            text: "social"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'SocialScreen'
        Button:
            text: "near you"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'NearYouScreen'
        
            
 
<FeedScreen>:
    Label:
        text: "feed"
    BoxLayout:
        orentation: "horizontal"
        size_hint: (1,0.1)
        Button:
            text: "profile"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ProfileScreen'
                
        Button:
            text: "feed"
            
        Button:
            text: "explore"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ExploreScreen'
        Button:
            text: "social"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'SocialScreen'
        Button:
            text: "near you"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'NearYouScreen'
                    
<ExploreScreen>:
    Label:
        text: "Explore"
    BoxLayout:
        orentation: "horizontal"
        size_hint: (1,0.1)
        Button:
            text: "profile"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ProfileScreen'
                
        Button:
            text: "feed"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'FeedScreen'
        Button:
            text: "explore"
            
        Button:
            text: "social"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'SocialScreen'
        Button:
            text: "near you"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'NearYouScreen'
 
<SocialScreen>:
    Label:
        text: "Socail"
    BoxLayout:
        orentation: "horizontal"
        size_hint: (1,0.1)
        Button:
            text: "profile"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ProfileScreen'
                
        Button:
            text: "feed"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'FeedScreen'
        Button:
            text: "explore"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ExploreScreen'
        Button:
            text: "social"
            
        Button:
            text: "near you"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'NearYouScreen'
                    
<NearYouScreen>:
    Label:
        text: "Near You"
    BoxLayout:
        orentation: "horizontal"
        size_hint: (1,0.1)
        Button:
            text: "profile"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ProfileScreen'
                
        Button:
            text: "feed"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'FeedScreen'
        Button:
            text: "explore"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'ExploreScreen'
        Button:
            text: "social"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'SocialScreen'
            
        Button:
            text: "near you"
            
 

""")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
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
# The ScreenManager controls moving between screens
sm = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
sm.add_widget(ProfileScreen(name="ProfileScreen"))
sm.add_widget(FeedScreen(name="FeedScreen"))
sm.add_widget(ExploreScreen(name="ExploreScreen"))
sm.add_widget(SocialScreen(name="SocialScreen"))
sm.add_widget(NearYouScreen(name="NearYouScreen"))

class MyApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    MyApp().run()