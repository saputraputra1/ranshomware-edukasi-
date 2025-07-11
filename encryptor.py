from cryptography.fernet import Fernet
import os

def generate_key(password):
    return Fernet(Fernet.generate_key())

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted = key.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted)
        return True
    except Exception:
        return False

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        decrypted = key.decrypt(data)
        with open(file_path, 'wb') as file:
            file.write(decrypted)
        return True
    except Exception:
        return False

def get_all_files(target_dir):
    all_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
