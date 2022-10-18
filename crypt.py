import rsa
with open('cle_pub.pem', mode='rb') as publickey:
    keydata = publickey.read()
publickey = rsa.PublicKey.load_pkcs1(keydata)

message = input("Type your message here : ").encode('utf-8')

crypto = rsa.encrypt(message, publickey)

print(crypto)