import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Listbox, END
# tạo csdl nếu chưa tồn tại
def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TaiKhoan (
                TenDangNhap TEXT PRIMARY KEY,
                MatKhau TEXT NOT NULL,
                VaiTro TEXT NOT NULL,
                MaNguoiDung TEXT NOT NULL
            )
        ''')
        db.commit()

create_database()

def add_account(): # thêm tài khoản
    username = username_var.get()
    password = password_var.get()
    role = role_var.get()
    user_id = user_id_var.get()

    if username and password and role and user_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute('''
                    INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro, MaNguoiDung)
                    VALUES (?, ?, ?, ?)
                ''', (username, password, role, user_id))
                db.commit()
                messagebox.showinfo("Success", "Account has been added")
                clear_fields()
                load_accounts()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
    else:
        messagebox.showerror("Error", "All fields are required")

def update_account(): # sửa tài khoản
    username = username_var.get()
    password = password_var.get()
    role = role_var.get()
    user_id = user_id_var.get()

    if username and password and role and user_id:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                UPDATE TaiKhoan
                SET MatKhau = ?, VaiTro = ?, MaNguoiDung = ?
                WHERE TenDangNhap = ?
            ''', (password, role, user_id, username))
            db.commit()
            messagebox.showinfo("Success", "Account has been updated")
            clear_fields()
            load_accounts()
    else:
        messagebox.showerror("Error", "All fields are required")

def delete_account(): # xóa tài khoản
    username = username_var.get()

    if username:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                DELETE FROM TaiKhoan
                WHERE TenDangNhap = ?
            ''', (username,))
            db.commit()
            messagebox.showinfo("Success", "Account has been deleted")
            clear_fields()
            load_accounts()
    else:
        messagebox.showerror("Error", "Username is required")

def search_account():
    search_term = search_var.get()
    account_listbox.delete(0, END)
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM TaiKhoan WHERE
            TenDangNhap LIKE ? OR
            VaiTro LIKE ? OR
            MaNguoiDung LIKE ?
        ''', ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            account_listbox.insert(END, row)

def load_accounts():
    account_listbox.delete(0, END)
    account_listbox.insert(END, ("Tên đăng nhập", "Mật khẩu", "Vai trò", "Mã người dùng"))  # Thêm tiêu đề cột
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM TaiKhoan')
        for row in cursor.fetchall():
            account_listbox.insert(END, row)

def clear_fields():
    username_var.set("")
    password_var.set("")
    role_var.set("")
    user_id_var.set("")

def close_fullscreen(event=None):
    window.attributes("-fullscreen", False)

# Create main window
window = Tk()
window.title("Quản lý tài khoản")
window.attributes("-fullscreen", True)
window.bind("<Escape>", close_fullscreen)

# Variables to store input values
username_var = StringVar()
password_var = StringVar()
role_var = StringVar()
user_id_var = StringVar()

# tạo các lable và entry
qltk_label = Label(text="Quản lý tài khoản", font=("Arial", 20))
qltk_label.place(x=620, y=70, width=550, height=35)

Label(window, text="Tên đăng nhập", font=("Arial", 12)).place(x=20, y=200, width=150, height=25)
Entry(window, textvariable=username_var, font=("Arial", 12)).place(x=180, y=200, width=200, height=25)

Label(window, text="Mật khẩu", font=("Arial", 12)).place(x=20, y=240, width=150, height=25)
Entry(window, textvariable=password_var, show='*', font=("Arial", 12)).place(x=180, y=240, width=200, height=25)

Label(window, text="Vai trò", font=("Arial", 12)).place(x=20, y=280, width=150, height=25)
Entry(window, textvariable=role_var, font=("Arial", 12)).place(x=180, y=280, width=200, height=25)

Label(window, text="Mã người dùng", font=("Arial", 12)).place(x=20, y=320, width=150, height=25)
Entry(window, textvariable=user_id_var, font=("Arial", 12)).place(x=180, y=320, width=200, height=25)

# tạo nút
Button(window, text="Thêm", font=("Arial", 12), command=add_account).place(x=20, y=400, width=100, height=25)
Button(window, text="Sửa", font=("Arial", 12), command=update_account).place(x=130, y=400, width=100, height=25)
Button(window, text="Xóa", font=("Arial", 12), command=delete_account).place(x=240, y=400, width=100, height=25)

# tạo ô tìm kiếm
search_var = StringVar()
Entry(window, textvariable=search_var, font=("Arial", 12)).place(x=620, y=150, width=550, height=25)
Button(window, text="Tìm kiếm", command=search_account, font=("Arial", 12)).place(x=1200, y=150, width=100, height=25)

# tạo listbox và hiển thị tài khoản
account_listbox = Listbox(window, font=("Arial", 12))
account_listbox.place(x=420, y=200, width=1000, height=500)

# tạo nút thoát
Button(window, text="Thoát", font=("Arial", 12), command=window.quit).place(x=1350, y=750, width=80, height=25)

load_accounts()

window.mainloop()