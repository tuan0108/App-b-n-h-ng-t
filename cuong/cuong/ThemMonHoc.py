import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Listbox, END

def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HocPhan (
                MaHP TEXT PRIMARY KEY,
                TenHP TEXT NOT NULL,
                SoTinChi INTEGER NOT NULL
            )
        ''')
        db.commit()

create_database()

def add_subject():
    subject_id = subject_id_var.get()
    subject_name = subject_name_var.get()
    credits = credits_var.get()

    if subject_id and subject_name and credits:
        try:
            credits = int(credits)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tín chỉ phải là một số nguyên")
            return

        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO HocPhan (MaHP, TenHP, SoTinChi)
                    VALUES (?, ?, ?)
                ''', (subject_id, subject_name, credits))
                db.commit()
                messagebox.showinfo("Thành công", "Môn học đã được thêm")
                clear_fields()
                load_subjects()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã học phần đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các ô phải được nhập")

def update_subject():
    subject_id = subject_id_var.get()
    subject_name = subject_name_var.get()
    credits = credits_var.get()

    if subject_id and subject_name and credits:
        try:
            credits = int(credits)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tín chỉ phải là một số nguyên")
            return

        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE HocPhan
                SET TenHP = ?, SoTinChi = ?
                WHERE MaHP = ?
            ''', (subject_name, credits, subject_id))
            db.commit()
            messagebox.showinfo("Thành công", "Môn học đã được cập nhật")
            clear_fields()
            load_subjects()
    else:
        messagebox.showerror("Lỗi", "Tất cả các ô phải được nhập")

def delete_subject():
    subject_id = subject_id_var.get()

    if subject_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM HocPhan
                WHERE MaHP = ?
            ''', (subject_id,))
            db.commit()
            messagebox.showinfo("Thành công", "Môn học đã được xóa")
            clear_fields()
            load_subjects()
    else:
        messagebox.showerror("Lỗi", "Mã học phần là bắt buộc")

def search_subject():
    search_term = search_var.get()
    subject_listbox.delete(0, END)
    subject_listbox.insert(END, ("Mã học phần", "Tên học phần", "Số tín chỉ"))  # Thêm tiêu đề cột
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM HocPhan WHERE
            MaHP LIKE ? OR
            TenHP LIKE ? OR
            CAST(SoTinChi AS TEXT) LIKE ?
        ''', ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            subject_listbox.insert(END, row)

def load_subjects():
    subject_listbox.delete(0, END)
    subject_listbox.insert(END, ("Mã học phần", "Tên học phần", "Số tín chỉ"))  # Thêm tiêu đề cột
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM HocPhan')
        for row in cursor.fetchall():
            subject_listbox.insert(END, row)

def clear_fields():
    subject_id_var.set("")
    subject_name_var.set("")
    credits_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính và cấu hình giao diện
window = Tk()
window.title("Quản lý học phần")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
subject_id_var = StringVar()
subject_name_var = StringVar()
credits_var = StringVar()
search_var = StringVar()

# Tạo các nhãn và ô nhập liệu
Label(window, text="Quản lý môn học", font=("Arial", 20)).place(x=600, y=50, width=550, height=35)

Label(window, text="Mã học phần", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=subject_id_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Tên học phần", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=subject_name_var, font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Số tín chỉ", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=credits_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

# Tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=add_subject).place(x=20, y=340, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=update_subject).place(x=140, y=340, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=delete_subject).place(x=260, y=340, width=100, height=25)

# Tìm kiếm
Entry(window, textvariable=search_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", font=("Arial", 12), command=search_subject).place(x=1200, y=150, width=100, height=25)

# Danh sách môn học
subject_listbox = Listbox(window, font=("Arial", 12))
subject_listbox.place(x=420, y=200, width=1000, height=500)

# Nút thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

load_subjects()

window.mainloop()