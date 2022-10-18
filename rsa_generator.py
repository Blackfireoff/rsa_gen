import base64
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
    return base64.b64encode(crypto)

def decrypt(message):
    with open("cle_priv.pem", mode="rb") as cle:
        clepriv = cle.read()
    privatekey = rsa.PrivateKey.load_pkcs1(clepriv)
    msg_decrypt = rsa.decrypt(base64.b64decode(message), privatekey)
    return msg_decrypt


