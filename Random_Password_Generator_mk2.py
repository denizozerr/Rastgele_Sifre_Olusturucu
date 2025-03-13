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

    # Şifreyi GUI'de göster
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

    # Şifreyi masaüstüne kaydet
    save_password(password)


def save_password(password):
    file_name = entry_file_name.get().strip() or "sifre.txt"
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)
    with open(desktop_path, "w") as file:
        file.write(password)

    # Kaydedildiğini bildiren mesaj
    messagebox.showinfo("Başarılı", f"Şifre '{file_name}' dosyasına kaydedildi.")


def update_password():
    # Mevcut şifreyi al ve kaydet
    current_password = password_display.get()
    if current_password:
        save_password(current_password)
    else:
        messagebox.showwarning("Uyarı", "Güncellenecek bir şifre yok.")


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

    label_info = tk.Label(about_window, text="Made By Denizzr\n v.1.1",
                          font=("Calibri", 12), fg="white", bg="#1C1C1C", justify="center", wraplength=280)
    label_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    close_button = tk.Button(about_window, text="Kapat", command=about_window.destroy,
                             font=("Calibri", 10), bg="red", fg="white", width=10, height=2)
    close_button.grid(row=1, column=0, pady=10)


# GUI setup
root = tk.Tk()
root.title("Rastgele Şifre Oluşturucu")
root.configure(bg="#333333")  # Arka plan rengini açık gri olarak ayarladık

# Pencereyi ortala ve boyutlandır
window_width = 340
window_height = 280
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

# Etiket ve giriş kutularını yan yana yerleştiriyoruz
tk.Label(root, text="Kaç Harf Olsun?", font=("Calibri", 12), fg="cyan", bg="#141414", relief="solid", bd=2).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=5,
                                                                                                                 pady=5,
                                                                                                                 sticky="e")
entry_letters = tk.Entry(root, font=("Calibri", 12), fg="black", bg="white", relief="solid", bd=2)
entry_letters.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Kaç Sembol Olsun?", font=("Calibri", 12), fg="cyan", bg="#141414", relief="solid", bd=2).grid(
    row=1, column=0, padx=5, pady=5, sticky="e")
entry_symbols = tk.Entry(root, font=("Calibri", 12), fg="black", bg="white", relief="solid", bd=2)
entry_symbols.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Kaç Sayı Olsun?", font=("Calibri", 12), fg="cyan", bg="#141414", relief="solid", bd=2).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=5,
                                                                                                                 pady=5,
                                                                                                                 sticky="e")
entry_numbers = tk.Entry(root, font=("Calibri", 12), fg="black", bg="white", relief="solid", bd=2)
entry_numbers.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Dosya Adı (Masaüstü):", font=("Calibri", 12), fg="cyan", bg="#141414", relief="solid", bd=2).grid(
    row=3, column=0, padx=5, pady=5, sticky="e")
entry_file_name = tk.Entry(root, font=("Calibri", 12), fg="black", bg="white", relief="solid", bd=2)
entry_file_name.grid(row=3, column=1, padx=5, pady=5)

# Butonları yan yana yerleştirmek için bir Frame kullanıyoruz
button_frame = tk.Frame(root, bg="#333333")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Şifre Oluştur", command=generate_password, font=("Calibri", 12), bg="green", fg="white",
          relief="solid", bd=2).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Güncelle", command=update_password, font=("Calibri", 12), bg="blue", fg="white",
          relief="solid", bd=2).pack(side=tk.LEFT, padx=5)

password_display = tk.Entry(root, font=("Calibri", 12), fg="black", bg="#f0f0f0", relief="solid", bd=2,
                            width=40)  # Düzenlenebilir hale getirildi
password_display.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

tk.Button(root, text="Hakkında", command=lambda: show_about_window(root), font=("Calibri", 12), bg="#9602a1",
          fg="white", relief="solid", bd=2).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()