import rsa
import os

with open("cle_priv.pem", mode="rb") as cle:
    clepriv = cle.read()
privatekey = rsa.PrivateKey.load_pkcs1(clepriv)

with open("message_crypt.LML", mode="r") as f:
    msg_crypt = f.read()

msg_crypt = bytes(msg_crypt, 'utf-8')

msg_decrypt = rsa.decrypt(msg_crypt, privatekey)
print(msg_decrypt)
print("decryptage \n")