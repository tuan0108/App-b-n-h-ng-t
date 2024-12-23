import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, END
from tkinter import ttk

def them_tai_khoan():  # thêm tài khoản
    tendangnhap = tendangnhap_var.get()
    matkhau = matkhau_var.get()
    vaitro = vaitro_var.get()
    user_id = user_id_var.get()

    if tendangnhap and matkhau and vaitro and user_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro, MaNguoiDung)
                    VALUES (?, ?, ?, ?)
                ''', (tendangnhap, matkhau, vaitro, user_id))
                db.commit()
                messagebox.showinfo("Thành công", "Tài khoản đã được thêm")
                xoa_noi_dung()
                hien_thi_tai_khoan()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại")
    else:
        messagebox.showerror("Lỗi", "Phải nhập đầy đủ các ô")

def sua_tai_khoan():  # sửa tài khoản
    tendangnhap = tendangnhap_var.get()
    matkhau = matkhau_var.get()
    vaitro = vaitro_var.get()
    user_id = user_id_var.get()

    if tendangnhap and matkhau and vaitro and user_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE TaiKhoan
                SET MatKhau = ?, VaiTro = ?, MaNguoiDung = ?
                WHERE TenDangNhap = ?
            ''', (matkhau, vaitro, user_id, tendangnhap))
            db.commit()
            messagebox.showinfo("Thành công", "Tài khoản đã được sửa")
            xoa_noi_dung()
            hien_thi_tai_khoan()
    else:
        messagebox.showerror("Lỗi", "Phải nhập đầy đủ các ô")

def xoa_tai_khoan():  # xóa tài khoản
    tendangnhap = tendangnhap_var.get()

    if tendangnhap:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM TaiKhoan
                WHERE TenDangNhap = ?
            ''', (tendangnhap,))
            db.commit()
            messagebox.showinfo("Thành công", "Đã xóa tài khoản")
            xoa_noi_dung()
            hien_thi_tai_khoan()
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập không tồn tại")

def tim_kiem_tai_khoan():
    timkiem = timkiem_var.get()
    for row in taikhoan_treeview.get_children():
        taikhoan_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM TaiKhoan WHERE
            TenDangNhap LIKE ? OR
            VaiTro LIKE ? OR
            MaNguoiDung LIKE ?
        ''', ('%' + timkiem + '%', '%' + timkiem + '%', '%' + timkiem + '%'))
        for row in cursor.fetchall():
            taikhoan_treeview.insert("", END, values=row)

def hien_thi_tai_khoan():
    for row in taikhoan_treeview.get_children():
        taikhoan_treeview.delete(row)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM TaiKhoan')
        for row in cursor.fetchall():
            taikhoan_treeview.insert("", END, values=row)

def xoa_noi_dung():
    tendangnhap_var.set("")
    matkhau_var.set("")
    vaitro_var.set("")
    user_id_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Tạo cửa sổ chính và cấu hình giao diện
window = Tk()
window.title("Quản lý tài khoản")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)

# Biến lưu trữ giá trị nhập vào
tendangnhap_var = StringVar()
matkhau_var = StringVar()
vaitro_var = StringVar()
user_id_var = StringVar()
timkiem_var = StringVar()

# Tạo các nhãn và ô nhập liệu
qltk_label = Label(text="Quản lý tài khoản", font=("Arial", 20))
qltk_label.place(x=620, y=70, width=550, height=35)

Label(window, text="Tên đăng nhập", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=tendangnhap_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Mật khẩu", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=matkhau_var, show='*', font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Vai trò", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=vaitro_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

Label(window, text="Mã người dùng", font=("Arial", 12)).place(x=20, y=320, width=150, height=25)
Entry(window, textvariable=user_id_var, font=("Arial", 12)).place(x=180, y=320, width=200, height=25)

# Tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=them_tai_khoan).place(x=20, y=400, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=sua_tai_khoan).place(x=130, y=400, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=xoa_tai_khoan).place(x=240, y=400, width=100, height=25)

# Tạo ô tìm kiếm
Entry(window, textvariable=timkiem_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", command=tim_kiem_tai_khoan, font=("Arial", 12)).place(x=1200, y=150, width=100, height=25)

# Tạo Treeview và hiển thị tài khoản
columns = ("TenDangNhap", "MatKhau", "VaiTro", "MaNguoiDung")
taikhoan_treeview = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
taikhoan_treeview.heading("TenDangNhap", text="Tên đăng nhập")
taikhoan_treeview.heading("MatKhau", text="Mật khẩu")
taikhoan_treeview.heading("VaiTro", text="Vai trò")
taikhoan_treeview.heading("MaNguoiDung", text="Mã người dùng")

taikhoan_treeview.place(x=420, y=200, width=1000, height=500)

# Tạo nút thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

hien_thi_tai_khoan()

window.mainloop()