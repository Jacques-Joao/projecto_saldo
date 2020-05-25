from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from random import randint
from kivy.uix.widget import Widget


class Btn(Widget):

    def caixa_unitel(self, instance, value):
        self.value_unitel = value
        if self.value_unitel:
            print("Unitel Checkbox Checked")
        else:
            print("Unitel Checkbox Unchecked")
        return self.value_unitel

    def caixa_movicel(self, instance, value):
        self.value_movicel = value
        if self.value_movicel:
            print("Movicel Checkbox Checked")
        else:
            print("Movicel Checkbox Unchecked")
        return self.value_movicel

    def clicado(self):
        self.codigo = ''
        try:
            if self.value_unitel == self.value_movicel == True:
                print('Desmarque uma das redes.')
        except:
            print('Por favor, selecione apenas uma rede!')
            pass
        try:
            if self.value_unitel == self.value_movicel == False:
                print('Somente uma das caixas de marcação deve ser selecionada')
        except:
            print('Antes de inicar o programa, marque as 2 caixas e em seguida desmarque a rede não desejada!')
            pass
        else:
            if self.value_unitel and not self.value_movicel:
                print('Operadora Unitel selecioanado!')
                self.codigo = str('*100*')
                return self.codigo
            elif self.value_movicel and not self.value_unitel:
                print('Operadora Movicel Selecionada')
                self.codigo = str('*196*')
                return self.codigo
        finally:
            self.num = randint(100000000000, 999999999999)
            face = Interface()
            face.iniciar(saldo=self.num, rede=self.codigo)
            self.bora = face.iniciar
            return self.bora

    def validar(self):
        valores = Btn()
        self.caixa_unitel()
        self.caixa_movicel()
        valores.clicado(unitel=self.value_unitel, movicel=bool(self.caixa_movicel))
        return valores.clicado


class Interface(FloatLayout):
    btn = Btn()

    def iniciar(self, saldo, rede):
        self.saldo = saldo
        self.rede = rede
        print(f'Fui clicado! E o número gerado foi {self.saldo}')
        print(f'{self.rede}{self.saldo[0]}#')

    def parar(self):
        print('Parar')


class UttsApp(App):

    def build(self):
        self.icon = 'pngwing.com.png'
        return Interface()


if __name__ == '__main__':
    UttsApp().run()
