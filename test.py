from kivy.app import App
from kivy_garden.mapview import MapView
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Login Page



class NearYouScreen(Screen):
    pass

kv = Builder.load_file('NearYouScreen.kv')

class MyApp(App):
    def build(self):
        return kv

if __name__=='__main__':
    MyApp().run()