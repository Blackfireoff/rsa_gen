import rsa
import os

def crypt(message):
    message = message.encode("utf-8")
    with open('cle_pub.pem', mode='rb') as publickey:
        keydata = publickey.read()
    publickey = rsa.PublicKey.load_pkcs1(keydata)
    crypto = rsa.encrypt(message, publickey)
    with open("message_crypt.LML", mode="wb") as f:
        f.write(crypto)
    print(crypto)

def decrypt():
    with open("cle_priv.pem", mode="rb") as cle:
        clepriv = cle.read()
    privatekey = rsa.PrivateKey.load_pkcs1(clepriv)
    msg_crypt = open("message_crypt.LML", "rb").read()
    msg_decrypt = rsa.decrypt(msg_crypt, privatekey)
    print(msg_decrypt.decode('utf-8'))
    print("decryptage \n")

