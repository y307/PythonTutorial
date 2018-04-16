#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TextBot():
    def __init__(self, input):
        self.name = 'Jake'
        self.voice = 'no'
        self.input = input()
        self.output = ''

    def answer_the_question(self):
        series_init = ['...']
        series_hello = ['привет', 'hi', 'здорово']
        series_how_are_you = ['как дела', 'как дела?']
        for x in range(len(series_init)):
            if self.input.lower() == series_init[x]:
                self.output = 'Поболтаем?'
        for x in range(len(series_hello)):
            if self.input.lower() == series_hello[x]:
                self.output = 'Привет, как дела?'
        for x in range(len(series_how_are_you)):
            if self.input.lower() == series_how_are_you[x]:
                self.output = 'У меня хорошо'
