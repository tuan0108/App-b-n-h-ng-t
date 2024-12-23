import sqlite3
<<<<<<< HEAD
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, END
from tkinter import ttk
=======
from tkinter import *
from tkinter import messagebox
>>>>>>> 378bc23799f73c30bbe304117a4453f4378e937c

def them_mon_hoc():
    id_monhoc = id_monhoc_var.get()
    ten_monhoc = ten_monhoc_var.get()
    tinchi = tinchi_var.get()

    if id_monhoc and ten_monhoc and tinchi:
        try:
            tinchi = int(tinchi)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tín chỉ phải là một số nguyên")
            return

        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO HocPhan (MaHP, TenHP, SoTinChi)
                    VALUES (?, ?, ?)
                ''', (id_monhoc, ten_monhoc, tinchi))
                db.commit()
                messagebox.showinfo("Thành công", "Môn học đã được thêm")
                xoa_noi_dung()
                hien_thi_monhoc()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã học phần đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Tất cả các ô phải được nhập")

def sua_mon_hoc():
    id_monhoc = id_monhoc_var.get()
    ten_monhoc = ten_monhoc_var.get()
    tinchi = tinchi_var.get()

    if id_monhoc and ten_monhoc and tinchi:
        try:
            tinchi = int(tinchi)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tín chỉ phải là một số nguyên")
            return

        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE HocPhan
                SET TenHP = ?, SoTinChi = ?
                WHERE MaHP = ?
            ''', (ten_monhoc, tinchi, id_monhoc))
            db.commit()
            messagebox.showinfo("Thành công", "Môn học đã được cập nhật")
            xoa_noi_dung()
            hien_thi_monhoc()
    else:
        messagebox.showerror("Lỗi", "Tất cả các ô phải được nhập")

def xoa_mon_hoc():
    id_monhoc = id_monhoc_var.get()

    if id_monhoc:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM HocPhan
                WHERE MaHP = ?
            ''', (id_monhoc,))
            db.commit()
            messagebox.showinfo("Thành công", "Môn học đã được xóa")
            xoa_noi_dung()
            hien_thi_monhoc()
    else:
        messagebox.showerror("Lỗi", "Mã học phần là bắt buộc")

def tim_kiem_monhoc():
    timkiem = timkiem_var.get()
    for row in monhoc_treeview.get_children():
        monhoc_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM HocPhan WHERE
            MaHP LIKE ? OR
            TenHP LIKE ? OR
            CAST(SoTinChi AS TEXT) LIKE ?
        ''', ('%' + timkiem + '%', '%' + timkiem + '%', '%' + timkiem + '%'))
        for row in cursor.fetchall():
            monhoc_treeview.insert("", END, values=row)

def hien_thi_monhoc():
    for row in monhoc_treeview.get_children():
        monhoc_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM HocPhan')
        for row in cursor.fetchall():
            monhoc_treeview.insert("", END, values=row)

def xoa_noi_dung():
    id_monhoc_var.set("")
    ten_monhoc_var.set("")
    tinchi_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính và cấu hình giao diện
window = Tk()
window.title("Quản lý học phần")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
id_monhoc_var = StringVar()
ten_monhoc_var = StringVar()
tinchi_var = StringVar()
timkiem_var = StringVar()

# Tạo các nhãn và ô nhập liệu
Label(window, text="Quản lý môn học", font=("Arial", 20)).place(x=600, y=50, width=550, height=35)

Label(window, text="Mã học phần", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=id_monhoc_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Tên học phần", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=ten_monhoc_var, font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Số tín chỉ", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=tinchi_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

# Tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=them_mon_hoc).place(x=20, y=340, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=sua_mon_hoc).place(x=140, y=340, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=xoa_mon_hoc).place(x=260, y=340, width=100, height=25)

# Tìm kiếm
Entry(window, textvariable=timkiem_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", font=("Arial", 12), command=tim_kiem_monhoc).place(x=1200, y=150, width=100, height=25)

# Danh sách môn học
columns = ("MaHP", "TenHP", "SoTinChi")
monhoc_treeview = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
monhoc_treeview.heading("MaHP", text="Mã học phần")
monhoc_treeview.heading("TenHP", text="Tên học phần")
monhoc_treeview.heading("SoTinChi", text="Số tín chỉ")
monhoc_treeview.place(x=420, y=200, width=1000, height=500)

# Nút thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

hien_thi_monhoc()

window.mainloop()