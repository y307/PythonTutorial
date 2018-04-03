from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')


class CalculatorApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical', padding=6)
        gl = GridLayout(cols=4, spacing=3)

        bl.add_widget(Label(text='0'))

        gl.add_widget(Button(text='7'))
        gl.add_widget(Button(text='8'))
        gl.add_widget(Button(text='9'))
        gl.add_widget(Button(text='x'))

        gl.add_widget(Button(text='4'))
        gl.add_widget(Button(text='5'))
        gl.add_widget(Button(text='6'))
        gl.add_widget(Button(text='/'))

        gl.add_widget(Button(text='1'))
        gl.add_widget(Button(text='2'))
        gl.add_widget(Button(text='3'))
        gl.add_widget(Button(text='-'))

        gl.add_widget(Button(text='0'))
        gl.add_widget(Button(text='.'))
        gl.add_widget(Button(text='='))
        gl.add_widget(Button(text='+'))

        bl.add_widget(gl)

        return bl


if __name__ == '__main__':
    CalculatorApp().run()
