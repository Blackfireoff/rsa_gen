import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from rsa_generator import crypt, decrypt
import logging


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = loadUi(Path().joinpath("data", "ui", "mainwindow.ui"))
        self.window.show()
        self.init_ui()
        self.app.exec()

    def init_ui(self):
        self.window.act_crypt.triggered.connect(self.crypt)

    def crypt(self):
        crypted_message = crypt(self.window.TE_cleartext.toPlainText())
        self.window.TE_cryptedtext.set



window = MainWindow()
