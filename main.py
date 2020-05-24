from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from random import randint
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox


class Caixa(CheckBox):

    def caixa_unitel(self, instance, value):
        if value is True:
            print("Unitel Checkbox Checked")
        else:
            print("Unitel Checkbox Unchecked")

    def caixa_movicel(self, instance, value):
        if value is True:
            print("Movicel Checkbox Checked")
        else:
            print("Movicel Checkbox Unchecked")


class Btn(Widget):

    def clicado(self):
        self.num = randint(100000000000, 999999999999)
        face = Interface()
        face.iniciar(self.num)
        self.bora = face.iniciar
        # del face.iniciar
        return self.bora


class Interface(FloatLayout):
    btn = Btn()
    cxa = Caixa()

    def iniciar(self, *algo):
        self.continuar = True
        # while self.continuar:
        self.inicio = algo[0]
        print(f'Fui clicado! E o número gerado foi {self.inicio}')
        # Clock
        # print(Clock)

    def parar(self):
        print('Parar')
        self.continuar = False

    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")



class UttsApp(App):

    def build(self):
        self.icon = 'pngwing.com.png'
        return Interface()


if __name__ == '__main__':
    UttsApp().run()
