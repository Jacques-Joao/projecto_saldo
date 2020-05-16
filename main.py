from kivy.uix.label import Label
from kivy.app import App

class UttsApp(App):

    def build(self):
        return Label(text="First Steps")

if __name__ == '__main__':
    UttsApp().run()

