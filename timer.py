import threading
import os
import time

def start_timer(duration, target_dir, status_callback):
    def countdown():
        for i in range(duration, 0, -1):
            status_callback(f"Timer: {i} detik")
            time.sleep(1)
        # Auto delete
        for root, _, files in os.walk(target_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass
        status_callback("File dihapus otomatis setelah waktu habis!")
    threading.Thread(target=countdown).start()
