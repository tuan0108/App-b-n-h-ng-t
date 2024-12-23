import sqlite3

# Tạo kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('feedback.db')

# Tạo con trỏ
c = conn.cursor()

# Tạo bảng giảng viên
c.execute('''
CREATE TABLE IF NOT EXISTS giangvien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten TEXT NOT NULL,
    monhoc TEXT NOT NULL
)
''')

# Tạo bảng đánh giá
c.execute('''
CREATE TABLE IF NOT EXISTS danhgia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    giangvien_id INTEGER NOT NULL,
    mucdo INTEGER NOT NULL,
    phanhoi TEXT,
    FOREIGN KEY (giangvien_id) REFERENCES giangvien(id)
)
''')

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# Hàm để thêm giảng viên mới vào cơ sở dữ liệu
def add_teacher():
    name = entry_new_name.get()
    subject = entry_new_subject.get()

    if not name or not subject:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin giảng viên!")
        return

    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('INSERT INTO giangvien (ten, monhoc) VALUES (?, ?)', (name, subject))
    conn.commit()
    conn.close()

    load_teachers()
    entry_new_name.delete(0, tk.END)
    entry_new_subject.delete(0, tk.END)
    messagebox.showinfo("Thông tin", "Thêm giảng viên thành công!")


# Hàm để tải danh sách giảng viên
def load_teachers():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT id, ten || " - " || monhoc FROM giangvien')
    teachers = c.fetchall()
    conn.close()

    combo_teacher['values'] = [t[1] for t in teachers]
    global teacher_map
    teacher_map = {t[1]: t[0] for t in teachers}


# Hàm để gửi đánh giá
def submit_feedback():
    teacher = combo_teacher.get()
    overall_rating = scale_overall.get()
    feedback = text_feedback.get("1.0", tk.END)

    if not teacher:
        messagebox.showerror("Lỗi", "Vui lòng chọn giảng viên!")
        return

    teacher_id = teacher_map[teacher]

    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('INSERT INTO danhgia (giangvien_id, mucdo, phanhoi) VALUES (?, ?, ?)',
              (teacher_id, overall_rating, feedback))
    conn.commit()
    conn.close()

    messagebox.showinfo("Thông tin", "Cảm ơn bạn đã đánh giá!")
    combo_teacher.set('')
    scale_overall.set(3)
    text_feedback.delete("1.0", tk.END)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đánh Giá Giảng Viên")
root.state('zoomed')  # Mở cửa sổ ở chế độ toàn màn hình

# Tạo khung nhập liệu
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Điều chỉnh để khung chiếm toàn bộ diện tích
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Frame cho đánh giá giảng viên
feedback_frame = ttk.LabelFrame(main_frame, text="Đánh Giá Giảng Viên", padding="20")
feedback_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

# Chọn giảng viên
ttk.Label(feedback_frame, text="Chọn giảng viên:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
combo_teacher = ttk.Combobox(feedback_frame, width=47)
combo_teacher.grid(row=0, column=1, pady=5, padx=5)

# Mức độ hài lòng chung
ttk.Label(feedback_frame, text="Mức độ hài lòng chung:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
scale_overall = ttk.Scale(feedback_frame, from_=1, to=5, orient=tk.HORIZONTAL)
scale_overall.set(3)
scale_overall.grid(row=1, column=1, pady=5, padx=5)

# Phản hồi chung
ttk.Label(feedback_frame, text="Phản hồi chung:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
text_feedback = tk.Text(feedback_frame, width=50, height=10)
text_feedback.grid(row=2, column=1, pady=5, padx=5)

# Nút gửi đánh giá
button_submit = ttk.Button(feedback_frame, text="Gửi đánh giá", command=submit_feedback)
button_submit.grid(row=3, column=1, pady=10, padx=5, sticky=tk.E)

# Frame cho thêm giảng viên mới
add_teacher_frame = ttk.LabelFrame(main_frame, text="Thêm Giảng Viên Mới", padding="20")
add_teacher_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

# Tên giảng viên mới
ttk.Label(add_teacher_frame, text="Tên giảng viên:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_new_name = ttk.Entry(add_teacher_frame, width=50)
entry_new_name.grid(row=0, column=1, pady=5, padx=5)

# Môn học giảng viên mới
ttk.Label(add_teacher_frame, text="Môn học:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_new_subject = ttk.Entry(add_teacher_frame, width=50)
entry_new_subject.grid(row=1, column=1, pady=5, padx=5)

# Nút thêm giảng viên mới
button_add_teacher = ttk.Button(add_teacher_frame, text="Thêm giảng viên", command=add_teacher)
button_add_teacher.grid(row=2, column=1, pady=10, padx=5, sticky=tk.E)

# Tải danh sách giảng viên khi mở ứng dụng
load_teachers()

# Chạy vòng lặp chính của Tkinter
root.mainloop()
