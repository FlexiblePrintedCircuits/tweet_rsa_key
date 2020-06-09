from Crypto.PublicKey import RSA
 
private_key = RSA.generate(1024)
with open('private_key.pem', 'w') as f:
    f.write(private_key.export_key().decode('utf-8'))

public_key = private_key.publickey()
with open('public_key.pem', 'w') as f:
    f.write(public_key.export_key().decode('utf-8'))