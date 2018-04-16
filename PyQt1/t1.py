#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QAction, QMessageBox, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QIcon('../pythonlogo.jpg'))

        extractAction = QAction('Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)

        self.toolBar1 = self.addToolBar('Extraction')

        self.home()

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())

        extractAction = QAction(QIcon('../pythonlogo.jpg'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar1.addAction(extractAction)

        btn.move(0, self.mainMenu.height()+self.toolBar1.height())

        checkBox = QCheckBox('Enlarge Window', self)
        checkBox.move(100, 25)
        checkBox.move(btn.width()+10, btn.pos().y()-3)
        checkBox.setAutoFillBackground(True)
        checkBox.stateChanged.connect(self.enlarge_window)
        # depending on what you want the default to be.
        # heckBox.toggle()

        self.show()

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QMessageBox.question(self,
                                      'Extract!',
                                      "Get into the chopper?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
