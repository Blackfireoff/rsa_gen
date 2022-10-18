import rsa
(pubkey,privkey) = rsa.newkeys(4096)

fichier = open("cle_pub.pem","a")
fichier.write(str(pubkey))
fichier.close()

fichier = open("cle_priv.pem","a")
fichier.write(str(privkey))
fichier.close()