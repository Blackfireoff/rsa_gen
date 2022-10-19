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
        self.dialogexec=0
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
            self.window.L_no_pubkey.setText('')
        except Exception as e:
            print(e)
            self.window.L_no_pubkey.setText('<font color=\'red\'><strong> Aucune clé <br> publique <br> importée !</strong></font>')

    def decrypt(self):
        try:
            clear_message = decrypt(self.window.TE_cryptedtext.toPlainText().encode("utf-8"),self.window.TE_privkey.toPlainText())
            self.window.TE_cleartext.setText(clear_message.decode("utf-8"))
            self.window.L_no_privkey.setText('')
        except Exception as e:
            print(e)
            self.window.L_no_privkey.setText('<font color=\'red\'><strong> Aucune clé <br> privée <br> importée !</strong></font>')

    def gen_keys(self):
        try:
            generation(int(self.window.CB_nbit.currentText()))
        except Exception as e:
            print(e)

    def click_on_pubkey(self):
        if not self.dialogexec:
            self.dialogexec=1
            fileNames = self.open_dialog()
            if fileNames:
                self.window.TE_pubkey.setText(fileNames[0])
            self.dialogexec = 0

    def click_on_privkey(self):
        if not self.dialogexec:
            self.dialogexec = 1
            fileNames=self.open_dialog()
            if fileNames:
                self.window.TE_privkey.setText(fileNames[0])
            self.dialogexec = 0

    def open_dialog(self):
        fileNames=[]
        dialog = QFileDialog(self.window)
        dialog.show()
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        return fileNames




window = MainWindow()
