import tkinter as tk
from PIL import Image, ImageTk  

root = tk.Tk()
root.title("Phần mềm chấm công")
root.geometry("500x300") 

frame = tk.Frame(root)
frame.pack(pady=20)

image1 = Image.open("add-user.png") 
photo1 = ImageTk.PhotoImage(image1)
button1 = tk.Button(frame, image=photo1, text="Thêm người dùng", compound="top")
button1.pack(side="left", padx=10) 
button1.image = photo1

image2 = Image.open("remove-user.png")
photo2 = ImageTk.PhotoImage(image2)
button2 = tk.Button(frame, image=photo2, text="Xóa người dùng", compound="top")
button2.pack(side="left", padx=10)
button2.image = photo2

image7 = Image.open("login-user.png")
photo7 = ImageTk.PhotoImage(image7)
button7 = tk.Button(frame, image=photo7, text="Đăng nhập tài khoản quản lý", compound="top")
button7.pack(side="left", padx=10)
button7.image = photo7


frame1 = tk.Frame(root)
frame1.pack(pady=20)

image3 = Image.open("check-in.png") 
photo3 = ImageTk.PhotoImage(image3)
button3 = tk.Button(frame1, image=photo3, text="Check-in", compound="top")
button3.pack(side="left", padx=10)
button3.image = photo3

image4 = Image.open("check-out.png")
photo4 = ImageTk.PhotoImage(image4)
button4 = tk.Button(frame1, image=photo4, text="Check-out", compound="top")
button4.pack(side="left", padx=10)
button4.image = photo4

image6 = Image.open("list-user.png")
photo6 = ImageTk.PhotoImage(image6)
button6 = tk.Button(frame1, image=photo6, text="Danh sách người dùng", compound="top")
button6.pack(side="left", padx=10)
button6.image = photo6

image5 = Image.open("history.png")
photo5 = ImageTk.PhotoImage(image5)
button5 = tk.Button(frame1, image=photo5, text="Lịch sử chấm công", compound="top")
button5.pack(side="left", padx=10)
button5.image = photo5

# Bắt đầu vòng lặp giao diện
root.mainloop()
