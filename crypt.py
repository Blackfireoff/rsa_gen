import rsa
with open('cle_pub.pem', mode='rb') as publickey:
    keydata = publickey.read()
publickey = rsa.PublicKey.load_pkcs1(keydata)

message = input("Type your message here : ").encode('utf-8')

crypto = rsa.encrypt(message, publickey)

#signature = rsa.sign(crypto,publickey, 'SHA-1')

#if(rsa.verify(message, signature, publickey) ==  'SHA-1'):
#    print("Signature vérifié")

with open("message_crypt.LML", mode="wb") as f:
    f.write(crypto)

print(crypto)