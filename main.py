from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from random import randint
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

value_unitel = False
value_movicel = False
txt = 0
texto = ''


class Btn(Widget):

    def caixa_unitel(self, value):
        global value_unitel
        value_unitel = value
        print('Unitel', value_unitel)

    def caixa_movicel(self, value):
        global value_movicel
        value_movicel = value
        print('Movicel', value_movicel)

    def clicado(self):
        self.codigo = self.validar()
        self.face = Interface()
        if not self.codigo:
            global texto
            if txt == 0:
                texto = 'Impossivel selecionar 2 redes. Por favor, selecione apenas uma rede!'
                print(texto)
                # msg()
            elif txt == 1:
                texto = 'Uma das caixas de marcação deve ser selecionada. Por favor, selecione apenas uma rede!'
                print(texto)
                # msg()
            else:
                texto = 'Algo de errado não está certo!'
                print(texto)
                # msg()
            pass
        else:
            self.num = randint(100000000000, 999999999999)
            self.face.iniciar(saldo=self.num, rede=self.codigo)
            return self.face.iniciar


    def validar(self):
        global value_unitel, value_movicel, txt
        self.value_unitel = value_unitel
        self.value_movicel = value_movicel
        if self.value_unitel == self.value_movicel == True:
            # print('Impossivel selecionar 2 redes.', end='')
            # print('Por favor, selecione apenas uma rede!')
            txt = 0
            return False
        elif self.value_unitel == self.value_movicel == False:
            # print('Uma das caixas de marcação deve ser selecionada')
            # print('Por favor, selecione apenas uma rede!')
            txt = 1
            return False
        else:
            if self.value_unitel and not self.value_movicel:
                print('Operadora Unitel selecioanado!')
                return str('*100*')
            elif not self.value_unitel and self.value_movicel:
                print('Operadora Movicel Selecionada')
                return str('*196*')


class Interface(FloatLayout):
    btn = Btn()

    def iniciar(self, saldo, rede):
        self.saldo = saldo
        self.rede = rede
        print(f'Fui clicado! E o número gerado foi {self.saldo}')
        print(f'{self.rede}{self.saldo}#')

    def parar(self):
        print('Parar')

def msg():
    show = Interface()
    mensagem = Popup(title='Aviso!', content='Hello', pos_hint=(0.5, 0.5), size_hint=(0.4, 0.2))
    mensagem.open()


class UttsApp(App):

    def build(self):
        self.icon = 'pngwing.com.png'
        return Interface()

    # def chamada(dt):
    #     global press
    #     if press == 0:
    #         Clock.


if __name__ == '__main__':
    UttsApp().run()
