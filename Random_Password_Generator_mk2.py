import random
import tkinter as tk
from tkinter import messagebox, Toplevel
import ctypes
import os


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&*+.?'

    try:
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())
    except ValueError:
        messagebox.showerror("Geçersiz giriş", "Lütfen sadece rakamlar giriniz")
        return

    password_list = (
            [random.choice(letters) for _ in range(nr_letters)] +
            [random.choice(symbols) for _ in range(nr_symbols)] +
            [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)
    password = ''.join(password_list)

    # Şifreyi masaüstüne kaydet
    file_name = entry_file_name.get().strip() or "sifre.txt"
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)
    with open(desktop_path, "w") as file:
        file.write(password)

    # Şifreyi GUI'de göster
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

    # Kaydedildiğini bildiren mesaj
    messagebox.showinfo("Başarılı", f"Şifre '{file_name}' dosyasına kaydedildi.")


def show_about_window(parent):
    about_window = Toplevel(parent)
    about_window.title("Hakkında")
    window_width = 300
    window_height = 150
    screen_width = about_window.winfo_screenwidth()
    screen_height = about_window.winfo_screenheight()

    # Ortada olacak şekilde pencereyi konumlandır
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    # Pencereyi bu pozisyonda aç
    about_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    about_window.configure(bg="#1C1C1C")
    about_window.iconbitmap(r"password.ico")
    about_window.attributes('-topmost', True)

    # Grid yapılandırması
    about_window.grid_rowconfigure(0, weight=1)
    about_window.grid_rowconfigure(1, weight=1)
    about_window.grid_columnconfigure(0, weight=1)

    label_info = tk.Label(about_window, text="Made By Denizzr\n v.1.7",
                          font=("Calibri", 12), fg="white", bg="#1C1C1C", justify="center", wraplength=280)
    label_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    close_button = tk.Button(about_window, text="Kapat", command=about_window.destroy,
                             font=("Calibri", 10), bg="red", fg="white", width=10, height=2)
    close_button.grid(row=1, column=0, pady=10)


# GUI setup
root = tk.Tk()
root.title("Rastgele Şifre Oluşturucu")

# Pencereyi ortala ve boyutlandır
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(True, True)
root.iconbitmap(r"password.ico")
root.attributes('-topmost', True)

# Windows karanlık modu
try:
    root.update_idletasks()
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE,
                                               ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int(1)))
except:
    pass

tk.Label(root, text="Kaç harf?").pack()
entry_letters = tk.Entry(root)
entry_letters.pack()

tk.Label(root, text="Kaç sembol?").pack()
entry_symbols = tk.Entry(root)
entry_symbols.pack()

tk.Label(root, text="Kaç sayı?").pack()
entry_numbers = tk.Entry(root)
entry_numbers.pack()

tk.Label(root, text="Dosya adı (Masaüstü):").pack()
entry_file_name = tk.Entry(root)
entry_file_name.pack()

tk.Button(root, text="Şifre Oluştur", command=generate_password).pack()

password_display = tk.Entry(root)  # Düzenlenebilir hale getirildi
password_display.pack()

tk.Button(root, text="Hakkında", command=lambda: show_about_window(root)).pack()

root.mainloop()