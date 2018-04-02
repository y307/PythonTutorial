#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class MyApp(App):

    def build(self):
        s = Scatter()
        fl = FloatLayout(size=(300, 300))
        fl.add_widget(Button(text='Это кнопка',
                             font_size=16,
                             on_press=self.btn_press,
                             background_color=[0, 0, 1, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(640/2-(640*.5/2), 480/2-(480*.25/2))))
        s.add_widget(fl)
        return s

    def btn_press(self, instance):
        instance.text = 'Я нажата!'


if __name__ == '__main__':
    MyApp().run()
