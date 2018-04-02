#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        return Button(text='Это кнопка',
                      background_color=(0, 0, 1, 1),
                      font_size=30,
                      on_press=self.btn_press)

    def btn_press(self, instance):
        instance.text = 'Я нажата!'


if __name__ == '__main__':
    MyApp().run()

