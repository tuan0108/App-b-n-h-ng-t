import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, END
from tkinter import ttk

def them_lop():
    id_lop = id_lop_var.get()
    ten_lop = ten_lop_var.get()
    id_giangvien = id_giangvien_var.get()

    if id_lop and ten_lop and id_giangvien:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO Lop (MaLop, TenLop, MaGVPT)
                    VALUES (?, ?, ?)
                ''', (id_lop, ten_lop, id_giangvien))
                db.commit()
                messagebox.showinfo("Thành công", "Lớp học đã được thêm")
                xoa_noi_dung()
                hien_thi_lop()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã lớp đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Phải nhập tất cả các ô")

def sua_lop():
    id_lop = id_lop_var.get()
    ten_lop = ten_lop_var.get()
    id_giangvien = id_giangvien_var.get()

    if id_lop and ten_lop and id_giangvien:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE Lop
                SET TenLop = ?, MaGVPT = ?
                WHERE MaLop = ?
            ''', (ten_lop, id_giangvien, id_lop))
            db.commit()
            messagebox.showinfo("Thành công", "Lớp học đã được cập nhật")
            xoa_noi_dung()
            hien_thi_lop()
    else:
        messagebox.showerror("Lỗi", "Phải nhập tất cả các ô")

def xoa_lop():
    id_lop = id_lop_var.get()

    if id_lop:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM Lop
                WHERE MaLop = ?
            ''', (id_lop,))
            db.commit()
            messagebox.showinfo("Thành công", "Lớp học đã được xóa")
            xoa_noi_dung()
            hien_thi_lop()
    else:
        messagebox.showerror("Lỗi", "Mã lớp là bắt buộc")

def tim_kiem_lop():
    timkiem = timkiem_var.get()
    for row in lop_treeview.get_children():
        lop_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM Lop WHERE
            MaLop LIKE ? OR
            TenLop LIKE ? OR
            MaGVPT LIKE ?
        ''', ('%' + timkiem + '%', '%' + timkiem + '%', '%' + timkiem + '%'))
        for row in cursor.fetchall():
            lop_treeview.insert("", END, values=row)

def hien_thi_lop():
    for row in lop_treeview.get_children():
        lop_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Lop')
        for row in cursor.fetchall():
            lop_treeview.insert("", END, values=row)

def xoa_noi_dung():
    id_lop_var.set("")
    ten_lop_var.set("")
    id_giangvien_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính
window = Tk()
window.title("Quản lý lớp học")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)
window.configure(bg='#f0f0f0')

# Biến lưu trữ giá trị nhập vào
id_lop_var = StringVar()
ten_lop_var = StringVar()
id_giangvien_var = StringVar()
timkiem_var = StringVar()

# Tạo các nhãn và ô nhập liệu
qll_label = Label(text="Quản lý lớp", font=("Arial", 20))
qll_label.place(x=620, y=70, width=550, height=35)

Label(window, text="Mã lớp", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=id_lop_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Tên lớp", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=ten_lop_var, font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Mã GV phụ trách", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=id_giangvien_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

# Tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=them_lop).place(x=20, y=400, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=sua_lop).place(x=130, y=400, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=xoa_lop).place(x=240, y=400, width=100, height=25)

# Tạo ô tìm kiếm
Entry(window, textvariable=timkiem_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", command=tim_kiem_lop, font=("Arial", 12)).place(x=1200, y=150, width=100, height=25)

# Tạo Treeview và hiển thị danh sách lớp học
columns = ("MaLop", "TenLop", "MaGVPT")
lop_treeview = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
lop_treeview.heading("MaLop", text="Mã lớp")
lop_treeview.heading("TenLop", text="Tên lớp")
lop_treeview.heading("MaGVPT", text="Mã GV phụ trách")

lop_treeview.place(x=420, y=200, width=1000, height=500)

# Tạo nút thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

hien_thi_lop()

window.mainloop()