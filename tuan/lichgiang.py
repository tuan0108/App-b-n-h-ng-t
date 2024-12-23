
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import sqlite3

# Tạo kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('feedback.db')

# Tạo con trỏ
c = conn.cursor()
# Tạo bảng lịch giảng
c.execute('''
CREATE TABLE IF NOT EXISTS lichgiang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    giangvien_id INTEGER NOT NULL,
    ngay TEXT NOT NULL,
    gio_bat_dau TEXT NOT NULL,
    gio_ket_thuc TEXT NOT NULL,
    phong TEXT NOT NULL,
    FOREIGN KEY (giangvien_id) REFERENCES giangvien(id)
)
''')

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()


# Hàm để tải danh sách giảng viên
def load_teachers():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT id, ten || " - " || monhoc FROM giangvien')
    teachers = c.fetchall()
    conn.close()

    combo_schedule_teacher['values'] = [t[1] for t in teachers]
    global teacher_map
    teacher_map = {t[1]: t[0] for t in teachers}


# Hàm để xem lịch giảng của giảng viên
def view_schedule():
    teacher = combo_schedule_teacher.get()

    if not teacher:
        messagebox.showerror("Lỗi", "Vui lòng chọn giảng viên!")
        return

    teacher_id = teacher_map[teacher]

    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT ngay, gio_bat_dau, gio_ket_thuc, phong FROM lichgiang WHERE giangvien_id = ?', (teacher_id,))
    schedule = c.fetchall()
    conn.close()

    for item in tree_schedule.get_children():
        tree_schedule.delete(item)

    if schedule:
        for row in schedule:
            tree_schedule.insert('', tk.END, values=row)
    else:
        messagebox.showinfo("Thông tin", "Không có lịch giảng.")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Xem Lịch Giảng")
root.geometry("800x600")

# Tạo khung nhập liệu
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Điều chỉnh để khung chiếm toàn bộ diện tích
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Chọn giảng viên
label_teacher = ttk.Label(frame, text="Chọn giảng viên:")
label_teacher.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
combo_schedule_teacher = ttk.Combobox(frame, width=50)
combo_schedule_teacher.grid(row=0, column=1, pady=10, padx=10)

# Nút xem lịch giảng
button_view_schedule = ttk.Button(frame, text="Xem Lịch Giảng", command=view_schedule)
button_view_schedule.grid(row=0, column=2, pady=10, padx=10)

# Tạo cây hiển thị lịch giảng
columns = ('Ngay', 'GioBatDau', 'GioKetThuc', 'Phong')
tree_schedule = ttk.Treeview(frame, columns=columns, show='headings')
tree_schedule.heading('Ngay', text='Ngày')
tree_schedule.heading('GioBatDau', text='Giờ Bắt Đầu')
tree_schedule.heading('GioKetThuc', text='Giờ Kết Thúc')
tree_schedule.heading('Phong', text='Phòng')

# Thêm thanh cuộn cho cây
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree_schedule.yview)
tree_schedule.configure(yscroll=scrollbar.set)
tree_schedule.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky=(tk.N, tk.S, tk.E, tk.W))
scrollbar.grid(row=1, column=3, pady=10, padx=10, sticky=(tk.N, tk.S))

# Điều chỉnh lưới để cây chiếm toàn bộ diện tích còn lại
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Tải danh sách giảng viên khi mở ứng dụng
load_teachers()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
