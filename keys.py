import rsa
(pubkey,privkey) = rsa.newkeys(1024)

print(pubkey)
print(type(pubkey))

with open("cle_pub.pem","wb") as f:
    f.write(pubkey.save_pkcs1('PEM')
    f.close()

with open("cle_priv.pem","wb") as f:
    f.write(privkey.save_pkcs1('PEM')
    f.close()

message = 'hello Bob!'.encode('utf8')

crypto = rsa.encrypt(message, pubkey)

print(crypto)