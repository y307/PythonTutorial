#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://python-3.ru/page/events-and-signals-in-pyqt5

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('Press key \"Q\" for close App', self)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        # if e.key() == Qt.Key_Escape:
        if e.key() == Qt.Key_Q:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
