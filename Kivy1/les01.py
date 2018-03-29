#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='Это кнопка')


if __name__ == '__main__':
    MyApp().run()
