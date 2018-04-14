#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://python-3.ru/page/pyqt5-create-widgets

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        lbl.move(60, 40)
        lbl.setText('Lable')

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
