#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
from PyQt5 import QtWidgets


class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


app = Application(sys.argv)

mw = MainWindow()
mw.resize(600, 500)
mw.setWindowTitle('PyQt5 App')
mw.show()

sys.exit(app.exec_())
