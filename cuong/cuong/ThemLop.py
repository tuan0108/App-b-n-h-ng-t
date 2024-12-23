import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Listbox, END

def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lop (
                MaLop TEXT PRIMARY KEY,
                TenLop TEXT NOT NULL,
                MaGVPT TEXT NOT NULL
            )
        ''')
        db.commit()

create_database()

def add_class():
    class_id = class_id_var.get()
    class_name = class_name_var.get()
    teacher_id = teacher_id_var.get()

    if class_id and class_name and teacher_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO Lop (MaLop, TenLop, MaGVPT)
                    VALUES (?, ?, ?)
                ''', (class_id, class_name, teacher_id))
                db.commit()
                messagebox.showinfo("Thành công", "Lớp học đã được thêm")
                clear_fields()
                load_classes()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã lớp đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")

def update_class():
    class_id = class_id_var.get()
    class_name = class_name_var.get()
    teacher_id = teacher_id_var.get()

    if class_id and class_name and teacher_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE Lop
                SET TenLop = ?, MaGVPT = ?
                WHERE MaLop = ?
            ''', (class_name, teacher_id, class_id))
            db.commit()
            messagebox.showinfo("Thành công", "Lớp học đã được cập nhật")
            clear_fields()
            load_classes()
    else:
        messagebox.showerror("Lỗi", "Tất cả các trường là bắt buộc")

def delete_class():
    class_id = class_id_var.get()

    if class_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM Lop
                WHERE MaLop = ?
            ''', (class_id,))
            db.commit()
            messagebox.showinfo("Thành công", "Lớp học đã được xóa")
            clear_fields()
            load_classes()
    else:
        messagebox.showerror("Lỗi", "Mã lớp là bắt buộc")

def search_class():
    search_term = search_var.get()
    class_listbox.delete(0, END)
    class_listbox.insert(END, ("Mã lớp", "Tên lớp", "Mã GV phụ trách"))  # Thêm tiêu đề cột
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM Lop WHERE
            MaLop LIKE ? OR
            TenLop LIKE ? OR
            MaGVPT LIKE ?
        ''', ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            class_listbox.insert(END, row)

def load_classes():
    class_listbox.delete(0, END)
    class_listbox.insert(END, ("Mã lớp", "Tên lớp", "Mã GV phụ trách"))  # Thêm tiêu đề cột
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Lop')
        for row in cursor.fetchall():
            class_listbox.insert(END, row)

def clear_fields():
    class_id_var.set("")
    class_name_var.set("")
    teacher_id_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính
window = Tk()
window.title("Quản lý lớp học")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
class_id_var = StringVar()
class_name_var = StringVar()
teacher_id_var = StringVar()

# Tạo các nhãn và ô nhập liệu
qll_label = Label(text="Quản lý lớp", font=("Arial", 20))
qll_label.place(x=620, y=70, width=550, height=35)

Label(window, text="Mã lớp", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=class_id_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Tên lớp", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=class_name_var, font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Mã GV phụ trách", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=teacher_id_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

# Tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=add_class).place(x=20, y=400, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=update_class).place(x=130, y=400, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=delete_class).place(x=240, y=400, width=100, height=25)
# tìm kiếm
search_var = StringVar()
Entry(window, textvariable=search_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", command=search_class, font=("Arial", 12)).place(x=1200, y=150, width=100, height=25)

# Tạo listbox và hiển thị danh sách lớp học
class_listbox = Listbox(window, font=("Arial", 12))
class_listbox.place(x=420, y=200, width=1000, height=500)

#thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

load_classes()

window.mainloop()