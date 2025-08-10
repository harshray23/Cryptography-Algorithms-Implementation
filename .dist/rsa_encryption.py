import rsa

(public_key, private_key) = rsa.newkeys(512)

message = "Sensitive data using RSA"

encrypted = rsa.encrypt(message.encode(), public_key)
print("Encrypted (RSA):", encrypted)

decrypted = rsa.decrypt(encrypted, private_key).decode()
print("Decrypted (RSA):", decrypted)
