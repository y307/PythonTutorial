from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter


class YTApp(App):

    def build(self):
        # fl = FloatLayout()
        btn = Button(text='Hello!',
                     # background_color=(0, 0, 1, 1),
                     font_size=100,
                     on_press = self.btn_press)
        # btn.bind(on_press=self.btn_press)
        # fl.add_widget(btn)
        return btn  # fl

    def btn_press(self, instance):
        print('!!!!!')
        instance.text = 'OPS!'


if __name__ == '__main__':
    YTApp().run()
