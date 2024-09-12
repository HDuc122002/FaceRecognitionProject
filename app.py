import tkinter as tk
from tkinter import messagebox
import admin
import checkin_checkout
import history

def login():
    login_window = tk.Toplevel(root)
    login_window.title("Đăng nhập Admin")

    username_label = tk.Label(login_window, text="Tên đăng nhập:")
    password_label = tk.Label(login_window, text="Mật khẩu:")
    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show='*')

    def process_login():
        username = username_entry.get()
        password = password_entry.get()
        if admin.check_login(username, password):
            messagebox.showinfo("Success", "Đăng nhập thành công")
            show_admin_menu()
            login_window.destroy()
        else:
            messagebox.showerror("Login Failed", "Thông tin đăng nhập không đúng")

    login_btn = tk.Button(login_window, text="Đăng nhập", command=process_login)

    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_btn.pack()

def show_admin_menu():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Panel")
    
    add_btn = tk.Button(admin_window, text="Thêm khuôn mặt", command=admin.add_face)
    delete_btn = tk.Button(admin_window, text="Xóa khuôn mặt", command=admin.delete_face)
    train_btn = tk.Button(admin_window, text="Huấn luyện mô hình", command=admin.train_model)
    view_people_btn = tk.Button(admin_window, text="Xem danh sách người dùng", command=admin.show_people)

    add_btn.pack(pady=10)
    delete_btn.pack(pady=10)
    train_btn.pack(pady=10)
    view_people_btn.pack(pady=10) 

def show_checkin():
    checkin_checkout.show_interface("checkin")

def show_checkout():
    checkin_checkout.show_interface("checkout")

def show_history():
    history.show_history()

root = tk.Tk()
root.title("Phần mềm chấm công")

login_btn = tk.Button(root, text="Đăng nhập", command=login)
checkin_btn = tk.Button(root, text="Checkin", command=show_checkin)
checkout_btn = tk.Button(root, text="Checkout", command=show_checkout)
history_btn = tk.Button(root, text="Lịch sử", command=show_history)

login_btn.pack(pady=10)
checkin_btn.pack(pady=10)
checkout_btn.pack(pady=10)
history_btn.pack(pady=10)

root.mainloop()
