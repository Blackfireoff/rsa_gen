import rsa
with open('cle_priv.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata)

