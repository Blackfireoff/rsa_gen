from Crypto.PublicKey import RSA

key = RSA.generate(1024)

with open('private.pem','w') as kf:
	kf.write(kf.decode())
	kf.close()

with open('public.pem','w') as pf:
	pf.write(pf.decode())
	pf.close()