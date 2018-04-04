from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.formula = ''
        self.lbl = Label(text='',
                         halign='right',
                         valign='center',
                         font_size=40,
                         text_size=(400-12, 500*.35-12),
                         size_hint=(1, .35))

    def update_lable(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_lable()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_lable()

    def calc_result(self, instance):
        res = str(eval(self.formula))
        self.formula += str(instance.text)+res
        self.update_lable()
        self.formula = "0"

    def build(self):
        bl = BoxLayout(orientation='vertical',
                       padding=6)

        gl = GridLayout(cols=4,
                        spacing=3,
                        size_hint=(1, .65))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='/', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.calc_result))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        bl.add_widget(gl)

        return bl
########################################################################


if __name__ == '__main__':
    CalculatorApp().run()
