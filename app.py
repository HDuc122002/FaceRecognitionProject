import tkinter as tk
from tkinter import messagebox
import admin
import checkin_checkout
from PIL import Image, ImageTk  

def login():
    login_window = tk.Toplevel(root)
    login_window.title("Đăng nhập")

    username_label = tk.Label(login_window, text="Tên đăng nhập:")
    password_label = tk.Label(login_window, text="Mật khẩu:")
    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show='*')

    def process_login():
        username = username_entry.get()
        password = password_entry.get()
        if admin.check_login(username, password):
            show_admin_menu()
            login_window.destroy()
        else:
            messagebox.showerror("Login Failed", "Thông tin đăng nhập không đúng")

    login_btn = tk.Button(login_window, text="Đăng nhập", command=process_login)

    username_label.pack(pady=5)
    username_entry.pack(padx=10)
    password_label.pack(pady=5)
    password_entry.pack(padx=10)
    login_btn.pack(pady=10)

def show_admin_menu():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin")
    
    add_btn = tk.Button(admin_window, text="Thêm khuôn mặt", command=admin.add_face, width=20, height=2)
    delete_btn = tk.Button(admin_window, text="Xóa khuôn mặt", command=admin.delete_face, width=20, height=2)
    train_btn = tk.Button(admin_window, text="Huấn luyện mô hình", command=admin.train_model, width=20, height=2)
    view_history_btn = tk.Button(admin_window, text="Lịch sử checkin/checkout", command=admin.show_history, width=20, height=2)
    view_people_btn = tk.Button(admin_window, text="Xem danh sách người dùng", command=admin.show_people, width=20, height=2)

    add_btn.pack(padx=10, pady=10)
    delete_btn.pack(padx=10, pady=10)
    train_btn.pack(padx=10, pady=10)
    view_history_btn.pack(padx=10, pady=10)
    view_people_btn.pack(padx=10, pady=10)

def show_checkin():
    checkin_checkout.show_interface("checkin")

def show_checkout():
    checkin_checkout.show_interface("checkout")


root = tk.Tk()
root.title("Phần mềm chấm công")
root.geometry("560x280")

login_image = Image.open("image/login-user.png")
login_photo = ImageTk.PhotoImage(login_image)
login_btn = tk.Button(root, image=login_photo, width=50, height=20, command=login)
login_btn.place(x=480, y=10)
login_btn.image = login_photo

frame = tk.Frame(root)
frame.pack(expand=True)

checkin_image = Image.open("image/check-in.png")
checkin_photo = ImageTk.PhotoImage(checkin_image)
checkin_btn = tk.Button(frame, image=checkin_photo, text="Checkin", compound="top", width=180, height=180, command=show_checkin)
checkin_btn.pack(side="left", padx=50)

checkout_image = Image.open("image/check-out.png")
checkout_photo = ImageTk.PhotoImage(checkout_image)
checkout_btn = tk.Button(frame, image=checkout_photo, text="Checkout", compound="top", width=180, height=180, command=show_checkout)
checkout_btn.pack(side="left", padx=50)

root.mainloop()