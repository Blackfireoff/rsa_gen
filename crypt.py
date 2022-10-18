import rsa
with open('cle_pub.pem', mode='r') as publickey:
    keydata = publickey.read()
publickey = rsa.key.PublicKey(keydata,1024)

print(publickey)
message = 'hello Bob!'.encode('utf8')

crypto = rsa.encrypt(message, publickey)

print(crypto)