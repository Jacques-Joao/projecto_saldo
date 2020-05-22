from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from random import randint


class Interface(FloatLayout, Widget):

    def clicado(self, **kwargs):
        self.num = randint(100000000000, 999999999999)
        return print(f'Fui clicado! E o número gerado foi {self.num}')



class UttsApp(App):

    def build(self):
        self.icon = 'pngwing.com.png'
        return Interface()


if __name__ == '__main__':
    UttsApp().run()
