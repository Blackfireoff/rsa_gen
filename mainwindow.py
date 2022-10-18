import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from rsa_generator import crypt, decrypt
from keys import generation
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
        self.window.act_gen_keys.triggered.connect(self.gen_keys)
        self.window.TE_pubkey.selectionChanged.connect(self.click_on_pubkey)
        self.window.TE_privkey.selectionChanged.connect(self.click_on_privkey)

    def crypt(self):
        try:
            crypted_message = crypt(self.window.TE_cleartext.toPlainText(),self.window.TE_pubkey.toPlainText())
            self.window.TE_cryptedtext.setText(crypted_message.decode("utf-8"))
        except Exception as e:
            print(e)

    def decrypt(self):
        try:
            clear_message = decrypt(self.window.TE_cryptedtext.toPlainText().encode("utf-8"),self.window.TE_privkey.toPlainText())
            self.window.TE_cleartext.setText(clear_message.decode("utf-8"))
        except Exception as e:
            print(e)

    def gen_keys(self):
        try:
            generation(int(self.window.CB_nbit.currentText()))
        except Exception as e:
            print(e)

    def click_on_pubkey(self):
        dialog = QFileDialog(self.window)
        dialog.show()
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        self.window.TE_pubkey.setText(fileNames[0])

    def click_on_privkey(self):
        dialog = QFileDialog(self.window)
        dialog.show()
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        self.window.TE_privkey.setText(fileNames[0])


window = MainWindow()
