import rsa

def generation(bits):
    (pubkey,privkey) = rsa.newkeys(bits)

    with open("cle_pub.pem","wb") as f:
        f.write(pubkey.save_pkcs1('PEM'))
        f.close()

    with open("cle_priv.pem","wb") as f:
        f.write(privkey.save_pkcs1('PEM'))
        f.close()
