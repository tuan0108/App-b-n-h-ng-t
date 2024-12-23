import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Frame, Toplevel, Listbox, Scrollbar, END

# Hàm để tạo cơ sở dữ liệu và bảng TaiKhoan nếu chưa tồn tại
def create_database():
    with sqlite3.connect("qlgv.db") as db:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TaiKhoan (
                TenDangNhap TEXT PRIMARY KEY,
                MaNguoiDung TEXT NOT NULL,
                MatKhau TEXT NOT NULL,
                VaiTro TEXT NOT NULL
            )
        ''')
        db.commit()

# Gọi hàm tạo cơ sở dữ liệu
create_database()

# Hàm để đăng ký tài khoản mới
def register_user(username_var, manguoidung_var, password_var, vaitro_var, register_window):
    print("Dùng form ThemTaiKhoan")
# Hàm để mở form Đăng ký
def open_register_form():
    print("Dùng form ThemTaiKhoan")

# Hàm để đăng nhập
def login_user(username_var, password_var):
    username = username_var.get()
    password = password_var.get()

    if username and password:
        with sqlite3.connect("qlgv.db") as db:
            cursor = db.cursor()
            cursor.execute('''
                SELECT MaNguoiDung, VaiTro FROM TaiKhoan
                WHERE TenDangNhap = ? AND MatKhau = ?
            ''', (username, password))
            result = cursor.fetchone()
            if result:
                manguoidung, vaitro = result
                with open("HienThi.txt", "w") as file:
                    file.write(f"MaNguoiDung: {manguoidung}\n")
                if vaitro == "admin":
                    open_admin_dashboard()
                elif vaitro == "giangvien":
                    open_giangvien_dashboard()
                elif vaitro == "sinhvien":
                    open_sinhvien_dashbroad()
                else:
                    messagebox.showerror("Lỗi", "Vai trò không hợp lệ")
            else:
                messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập và mật khẩu")

# Hàm để mở form Đăng nhập
def open_login_form():
    login_window = Tk()
    login_window.title("Đăng nhập")
    login_window.geometry("400x300")
    login_window.configure(bg='#f0f0f0')

    username_var = StringVar()
    password_var = StringVar()

    frame = Frame(login_window, bg='#ffffff', padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    Label(frame, text="Tên đăng nhập", font=("Arial", 14), bg='#ffffff').grid(row=0, column=0, pady=5, sticky='w')
    Entry(frame, textvariable=username_var, font=("Arial", 14)).grid(row=0, column=1, pady=5)

    Label(frame, text="Mật khẩu", font=("Arial", 14), bg='#ffffff').grid(row=1, column=0, pady=5, sticky='w')
    Entry(frame, textvariable=password_var, font=("Arial", 14), show='*').grid(row=1, column=1, pady=5)

    Button(frame, text="Đăng nhập", font=("Arial", 14),
           command=lambda: login_user(username_var, password_var),
           bg='#4caf50', fg='#ffffff').grid(row=2, column=0, columnspan=2, pady=10)

    Button(frame, text="Đăng ký", font=("Arial", 14),
           command=open_register_form,
           bg='#2196f3', fg='#ffffff').grid(row=3, column=0, columnspan=2, pady=10)

    login_window.mainloop()

# test Hàm để mở giao diện admin
def open_admin_dashboard():
    def open_subject_management():
        print("Mở form quản lý học phần")

    # Hàm mở form tài khoản (chưa triển khai)
    def open_account_form():
        print("Mở form tài khoản")

    # Hàm mở form giảng viên (chưa triển khai)
    def open_teacher_form():
        print("Mở form giảng viên")

    # Hàm mở form sinh viên (chưa triển khai)
    def open_student_form():
        print("Mở form sinh viên")

    # Hàm mở form lớp (chưa triển khai)
    def open_class_form():
        print("Mở form lớp")

    # Hàm mở form phân công (chưa triển khai)
    def open_assignment_form():
        print("Mở form phân công")

    # Hàm mở form đánh giá (chưa triển khai)
    def open_evaluation_form():
        print("Mở form đánh giá")

    # Hàm thoát fullscreen khi nhấn phím Esc
    def exit_fullscreen(event):
        if event.keysym == 'Escape':
            window.attributes('-fullscreen', False)
            window.unbind('<Escape>')
            window.bind('<Escape>', exit_app)  # Khi ấn Esc lần thứ 2 sẽ thoát ứng dụng

    # Hàm thoát ứng dụng khi nhấn Esc lần thứ 2 (đã thoát fullscreen)
    def exit_app(event):
        if event.keysym == 'Escape':
            window.destroy()

    # Tạo cửa sổ chính và cấu hình giao diện
    window = Tk()
    window.title("Main Dashboard - Admin")
    window.attributes('-fullscreen', True)  # Thiết lập fullscreen
    window.configure(bg='#ffffff')

    # Bắt sự kiện Esc để thoát fullscreen
    window.bind('<Escape>', exit_fullscreen)

    # Tạo Frame để chứa các nút chức năng, đặt ở bên trái
    menu_frame = Frame(window, bg='#ffffff', padx=20, pady=20)
    menu_frame.pack(side='left', fill='y')

    # Tạo các nút chức năng
    btn_account = Button(menu_frame, text="Tài khoản", font=("Arial", 12), width=15, height=2,
                         command=open_account_form)
    btn_account.pack(fill='x', pady=10)

    btn_teacher = Button(menu_frame, text="Giảng viên", font=("Arial", 12), width=15, height=2,
                         command=open_teacher_form)
    btn_teacher.pack(fill='x', pady=10)

    btn_student = Button(menu_frame, text="Sinh viên", font=("Arial", 12), width=15, height=2,
                         command=open_student_form)
    btn_student.pack(fill='x', pady=10)

    btn_class = Button(menu_frame, text="Lớp", font=("Arial", 12), width=15, height=2, command=open_class_form)
    btn_class.pack(fill='x', pady=10)

    btn_assignment = Button(menu_frame, text="Phân công", font=("Arial", 12), width=15, height=2,
                            command=open_assignment_form)
    btn_assignment.pack(fill='x', pady=10)

    btn_subject = Button(menu_frame, text="Học phần", font=("Arial", 12), width=15, height=2,
                         command=open_subject_management)
    btn_subject.pack(fill='x', pady=10)

    btn_evaluation = Button(menu_frame, text="Đánh giá", font=("Arial", 12), width=15, height=2,
                            command=open_evaluation_form)
    btn_evaluation.pack(fill='x', pady=10)

# Hàm để mở giao diện giảng viên
def open_giangvien_dashboard():
    print("Chào gv")
def open_sinhvien_dashbroad():
    print("Chào sv")

# Khởi chạy ứng dụng
open_login_form()