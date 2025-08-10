from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("aes.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("aes.key", "rb").read()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    return decrypted.decode()

if __name__ == "__main__":
    print("AES Encryption/Decryption")
    key = generate_key()
    message = "Confidential message to encrypt"
    print(f"\nOriginal message: {message}")
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")
