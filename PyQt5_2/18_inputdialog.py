#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://python-3.ru/page/dialogs-in-pyqt5

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.le = QLineEdit(self)
        self.btn = QPushButton('Dialog', self)
        self.initUI()

    def initUI(self):
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le.move(130, 20)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
