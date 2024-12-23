from tkinter import Tk, Button, Frame

# Hàm mở form quản lý học phần (chưa triển khai)
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
btn_account = Button(menu_frame, text="Tài khoản", font=("Arial", 12), width=15, height=2, command=open_account_form)
btn_account.pack(fill='x', pady=10)

btn_teacher = Button(menu_frame, text="Giảng viên", font=("Arial", 12), width=15, height=2, command=open_teacher_form)
btn_teacher.pack(fill='x', pady=10)

btn_student = Button(menu_frame, text="Sinh viên", font=("Arial", 12), width=15, height=2, command=open_student_form)
btn_student.pack(fill='x', pady=10)

btn_class = Button(menu_frame, text="Lớp", font=("Arial", 12), width=15, height=2, command=open_class_form)
btn_class.pack(fill='x', pady=10)

btn_assignment = Button(menu_frame, text="Phân công", font=("Arial", 12), width=15, height=2, command=open_assignment_form)
btn_assignment.pack(fill='x', pady=10)

btn_subject = Button(menu_frame, text="Học phần", font=("Arial", 12), width=15, height=2, command=open_subject_management)
btn_subject.pack(fill='x', pady=10)

btn_evaluation = Button(menu_frame, text="Đánh giá", font=("Arial", 12), width=15, height=2, command=open_evaluation_form)
btn_evaluation.pack(fill='x', pady=10)

# Chạy ứng dụng
window.mainloop()