from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


private_pem = None
private_key = None
public_pem = None
public_key = None


with open('private_key.pem', 'br') as f:
    private_pem = f.read()
    private_key = RSA.import_key(private_pem)


with open('public_key.pem', 'br') as f:
    public_pem = f.read()
    public_key = RSA.import_key(public_pem)


message = input() # 平文
public_cipher = PKCS1_OAEP.new(public_key)
ciphertext = public_cipher.encrypt(message.encode())
print(ciphertext) # 暗号文

private_cipher = PKCS1_OAEP.new(private_key)
decrypt_message = private_cipher.decrypt(ciphertext).decode("utf-8")
print(decrypt_message) # 復号分