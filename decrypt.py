import rsa
import os

with open("cle_priv.pem", mode="rb") as cle:
    clepriv = cle.read()
privatekey = rsa.PrivateKey.load_pkcs1(clepriv)

msg_crypt = open("message_crypt.LML","rb").read()


msg_decrypt = rsa.decrypt(msg_crypt, privatekey)
print(msg_decrypt.decode('utf-8'))
print("decryptage \n")