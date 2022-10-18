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
        self.window.act_decrypt.triggered.connect(self.decrypt)

    def crypt(self):
        try:
            crypted_message = crypt(self.window.TE_cleartext.toPlainText())
            self.window.TE_cryptedtext.setText(crypted_message.decode("utf-8"))
        except Exception as e:
            print(e)

    def decrypt(self):
        try:
            clear_message = decrypt(self.window.TE_cryptedtext.toPlainText().encode("utf-8"))
            self.window.TE_cleartext.setText(clear_message.decode("utf-8"))
        except Exception as e:
            print(e)



window = MainWindow()
