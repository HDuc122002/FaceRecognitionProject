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
    admin_window.title("Trang quản lý")

    frame = tk.Frame(admin_window)
    frame.pack(padx=20, pady=20)

    add_user_image = Image.open("image/add-user.png")
    add_user_photo = ImageTk.PhotoImage(add_user_image)
    delete_user_image = Image.open("image/delete-user.png")
    delete_user_photo = ImageTk.PhotoImage(delete_user_image)
    train_model_image = Image.open("image/train-model.png")
    train_model_photo = ImageTk.PhotoImage(train_model_image)
    history_image = Image.open("image/history-user.png")
    history_photo = ImageTk.PhotoImage(history_image)
    list_user_image = Image.open("image/list-user.png")
    list_user_photo = ImageTk.PhotoImage(list_user_image)

    add_btn = tk.Button(frame, text="Thêm khuôn mặt", image=add_user_photo, compound="top", command=admin.add_face, width=120, height=120)
    delete_btn = tk.Button(frame, text="Xóa khuôn mặt", image=delete_user_photo, compound="top", command=admin.delete_face, width=120, height=120)
    # train_btn = tk.Button(frame, text="Huấn luyện mô hình",image=train_model_photo, compound="top", command=admin.train_model, width=120, height=120)
    # history_btn = tk.Button(frame, text="Lịch sử", image=history_photo, compound="top", command=admin.show_history, width=120, height=120)
    # list_user_btn = tk.Button(frame, text="Danh sách nhân viên", image=list_user_photo, compound="top", command=admin.show_people, width=120, height=120)

    add_btn.image = add_user_photo
    delete_btn.image = delete_user_photo
    # train_btn.image = train_model_photo
    # history_btn.image = history_photo
    # list_user_btn.image = list_user_photo

    add_btn.grid(row=0, column=0, padx=10, pady=10)
    delete_btn.grid(row=0, column=1, padx=10, pady=10)
    # train_btn.grid(row=0, column=2, padx=10, pady=10)
    # history_btn.grid(row=1, column=0, padx=10, pady=10)
    # list_user_btn.grid(row=1, column=1, padx=10, pady=10)

    admin_window.geometry("500x350")

def show_checkin():
    checkin_checkout.show_interface("checkin")

def show_checkout():
    checkin_checkout.show_interface("checkout")

root = tk.Tk()
root.title("Face Recognition")
root.geometry("560x280")

login_image = Image.open("image/login-user.png")
login_photo = ImageTk.PhotoImage(login_image)

login_btn = tk.Button(root, image=login_photo, width=50, height=20, command=login)

login_btn.place(x=480, y=5)

login_btn.image = login_photo

frame = tk.Frame(root)
frame.pack(expand=True)

checkin_image = Image.open("image/check-in.png")
checkin_photo = ImageTk.PhotoImage(checkin_image)
checkout_image = Image.open("image/check-out.png")
checkout_photo = ImageTk.PhotoImage(checkout_image)

checkin_btn = tk.Button(frame, image=checkin_photo, text="Checkin", compound="top", width=200, height=200, command=show_checkin)
# checkout_btn = tk.Button(frame, image=checkout_photo, text="Checkout", compound="top", width=200, height=200, command=show_checkout)

checkin_btn.pack(side="left", padx=50)
# checkout_btn.pack(side="left", padx=(0,50))

checkin_btn.image = checkin_photo
# checkout_btn.image = checkout_photo

root.mainloop()