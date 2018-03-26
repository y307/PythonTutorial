#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://python-3.ru/page/dialogs-in-pyqt5

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.frm = QFrame(self)
        self.btn = QPushButton('Dialog', self)
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 20, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
