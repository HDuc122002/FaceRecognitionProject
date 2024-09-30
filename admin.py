from tkinter import messagebox
import queryDB as db
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import ttk 

def check_login(username, password):
    return db.check_admin_credentials(username, password)

def add_face():
    def submit_name():
        name = name_entry.get()
        if name:
            user_id = db.insert(name)

            cam = cv2.VideoCapture(0)
            cam.set(3, 1280)
            cam.set(4, 720)  

            detector = cv2.CascadeClassifier('libs/haarcascade_frontalface_default.xml')
            sampleNum = 0

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    sampleNum += 1
                    if not os.path.exists('dataSet'):
                        os.makedirs('dataSet')
                    cv2.imwrite(f"dataSet/User.{user_id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
                    cv2.imshow('image', img)

                if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum >= 100: 
                    break

            cam.release()
            cv2.destroyAllWindows()
            train_new_face(user_id)
            messagebox.showinfo("Thành công","Thêm khuôn mặt người dùng mới thành công")
            add_face_window.destroy()

    add_face_window = tk.Toplevel()
    add_face_window.title("Thêm Khuôn Mặt")

    name_label = tk.Label(add_face_window, text="Nhập tên người dùng:")
    name_entry = tk.Entry(add_face_window)
    submit_btn = tk.Button(add_face_window, text="Thêm", command=submit_name)
    cancel_btn = tk.Button(add_face_window, text="Hủy", command=add_face_window.destroy)

    name_label.pack(pady=5)
    name_entry.pack(pady=5)
    submit_btn.pack(side="left", padx=20, pady=5)
    cancel_btn.pack(side="left", padx=20, pady=5)

def train_new_face(user_id):
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    if os.path.exists('recognizer/trainningData.yml'):
        recognizer.read('recognizer/trainningData.yml')
    
    faces = []
    ids = []

    for image in os.listdir('dataSet'):
        if image.startswith(f'User.{user_id}.'):
            img_path = os.path.join('dataSet', image)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces.append(gray)
            ids.append(user_id)

    recognizer.update(faces, np.array(ids))
    
    recognizer.save('recognizer/trainningData.yml')


def delete_face():
    def submit_delete():
        user_id = name_entry.get()
        if not user_id.isdigit():
            messagebox.showerror("Lỗi", "ID người dùng không hợp lệ.")
            return
        
        user_id = int(user_id)
        delete_data = db.getProfile(user_id)

        if not delete_data:
                messagebox.showerror("Lỗi", "Người dùng không tồn tại.")
                return
        try:
            user_name = delete_data['name'] if 'name' in delete_data else 'Người dùng'
            images = [f for f in os.listdir('dataSet') if f.startswith(f'User.{user_id}.')]
            
            for image in images:
                os.remove(os.path.join('dataSet', image))
                
            db.deleteUser(user_id)
            messagebox.showinfo("Thành công", f"Đã xóa khuôn mặt của người dùng: {user_name}")
            delete_face_window.destroy()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa khuôn mặt: {e}")

    delete_face_window = tk.Toplevel()
    delete_face_window.title("Xóa Khuôn Mặt")

    name_label = tk.Label(delete_face_window, text="Nhập ID người dùng cần xóa:")
    name_entry = tk.Entry(delete_face_window)
    submit_btn = tk.Button(delete_face_window, text="Xóa", command=submit_delete)
    cancel_btn = tk.Button(delete_face_window, text="Hủy", command=delete_face_window.destroy)

    name_label.pack(pady=5)
    name_entry.pack(pady=5)
    submit_btn.pack(side="left",padx=(30,0),pady=5)
    cancel_btn.pack(side="left",padx=(30,0),pady=5)


def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    ids = []

    for image in os.listdir('dataSet'):
        img_path = os.path.join('dataSet', image)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        user_id = int(image.split('.')[1])
        
        faces.append(gray)
        ids.append(user_id)

    if not faces or not ids:
        messagebox.showerror("Lỗi", "Không có dữ liệu huấn luyện")
        return

    recognizer.train(faces, np.array(ids))

    recognizer.save('recognizer/trainningData.yml')
    messagebox.showinfo("Thành công","Huấn luyện mô hình thành công")

def show_people():
    people_data = db.get_people()

    people_window = tk.Toplevel()
    people_window.title("Danh Sách Người Dùng")
    people_window.geometry("600x400")

    columns = ('ID', 'Tên')
    tree = ttk.Treeview(people_window, columns=columns, show='headings')
    
    tree.heading('ID', text='ID')
    tree.heading('Tên', text='Tên')

    tree.column('ID', width=50, anchor="center")
    tree.column('Tên', width=150, anchor="center")

    tree.pack(expand=True, fill='both')

    if not people_data:
        no_data_label = tk.Label(people_window, text="Không có dữ liệu người dùng.")
        no_data_label.pack()
    else:
        for entry in people_data:
            tree.insert('', tk.END, values=(entry[0], entry[1]))

    tree.bind("<Configure>", lambda e: tree.configure(height=min(len(people_data), 10)))

def show_history():
    history_data = db.get_history()

    history_window = tk.Toplevel()
    history_window.title("Lịch sử Checkin/Checkout")
    history_window.geometry("600x400")

    columns = ('ID', 'Tên', 'Thời gian', 'Hành động')
    tree = ttk.Treeview(history_window, columns=columns, show='headings')
    
    tree.heading('ID', text='ID')
    tree.heading('Tên', text='Tên')
    tree.heading('Thời gian', text='Thời gian')
    tree.heading('Hành động', text='Hành động')

    tree.column('ID', width=50,anchor="center")
    tree.column('Tên', width=150,anchor="center")
    tree.column('Thời gian', width=200,anchor="center")
    tree.column('Hành động', width=100,anchor="center")

    tree.pack(expand=True, fill='both')

    if not history_data:
        no_data_label = tk.Label(history_window, text="Không có dữ liệu lịch sử.")
        no_data_label.pack()
    else:
        for entry in history_data:
            tree.insert('', tk.END, values=(entry[0], entry[1], entry[2], entry[3]))

    tree.bind("<Configure>", lambda e: tree.configure(height=min(len(history_data), 10)))