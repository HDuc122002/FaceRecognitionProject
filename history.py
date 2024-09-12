import queryDB as db
import tkinter as tk
from tkinter import ttk

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

    tree.column('ID', width=50)
    tree.column('Tên', width=150)
    tree.column('Thời gian', width=200)
    tree.column('Hành động', width=100)

    tree.pack(expand=True, fill='both')

    # Nếu không có dữ liệu, hiển thị một nhãn thông báo
    if not history_data:
        no_data_label = tk.Label(history_window, text="Không có dữ liệu lịch sử.")
        no_data_label.pack()
    else:
        for entry in history_data:
            tree.insert('', tk.END, values=(entry[0], entry[1], entry[2], entry[3]))

    # Đặt chiều cao của cây (tree) để có thể hiển thị tốt hơn
    tree.bind("<Configure>", lambda e: tree.configure(height=min(len(history_data), 10)))

