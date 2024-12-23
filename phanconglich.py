import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# Tạo cửa sổ chính
window = Tk()
window.title("Phân Công Lịch Giảng")
window.attributes('-fullscreen', True)
window.configure(bg="#f0f0f0")

# Hàm để phân công lịch giảng
def loaddulieuvaodatabase():
    idgv = entry_MaGV.get()
    idhp = entry_MaHP.get()
    hocky = entry_HocKy.get()
    nam = entry_NamHoc.get()
    idlop = entry_MaLop.get()

    db = sqlite3.connect('nam/qlgv.db')
    cursor = db.cursor()
    cursor.execute('INSERT INTO PhanCong (MaGV, MaHP, HocKy, NamHoc, MaLop) VALUES (?, ?, ?, ?, ?)',
                   (idgv, idhp, hocky, nam, idlop))
    db.commit()
    db.close()

    messagebox.showinfo("Thông tin", "Phân công lịch giảng thành công!")
    entry_MaGV.delete(0, END)
    entry_MaHP.delete(0, END)
    entry_HocKy.delete(0, END)
    entry_NamHoc.delete(0, END)
    entry_MaLop.delete(0, END)

# Hàm để thoát khỏi ứng dụng
def exit_app():
    window.destroy()

# Tạo khung chính chứa tất cả widget
main_frame = ttk.Frame(window, padding="20")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
main_frame.configure(style='MainFrame.TFrame')

# Tạo khung chứa các trường nhập liệu
input_frame = ttk.Frame(main_frame, padding="20", borderwidth=2, relief="solid")
input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Tạo style cho các widget
style = ttk.Style()
style.configure('MainFrame.TFrame', background='#f0f0f0')
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Arial', 14))
style.configure('TEntry', font=('Arial', 14))
style.configure('TButton', font=('Arial', 14), padding=10)

# Chọn giảng viên
label_MaGV = ttk.Label(input_frame, text="Mã giảng viên:")
label_MaGV.grid(row=0, column=0, sticky=E, padx=10, pady=10)
entry_MaGV = ttk.Entry(input_frame, width=30)
entry_MaGV.grid(row=0, column=1, pady=10, padx=10)

# Mã học phần
label_MaHP = ttk.Label(input_frame, text="Mã học phần:")
label_MaHP.grid(row=1, column=0, sticky=E, padx=10, pady=10)
entry_MaHP = ttk.Entry(input_frame, width=30)
entry_MaHP.grid(row=1, column=1, pady=10, padx=10)

# Học kỳ
label_HocKy = ttk.Label(input_frame, text="Học kỳ:")
label_HocKy.grid(row=2, column=0, sticky=E, padx=10, pady=10)
entry_HocKy = ttk.Entry(input_frame, width=30)
entry_HocKy.grid(row=2, column=1, pady=10, padx=10)

# Năm học
label_NamHoc = ttk.Label(input_frame, text="Năm học:")
label_NamHoc.grid(row=3, column=0, sticky=E, padx=10, pady=10)
entry_NamHoc = ttk.Entry(input_frame, width=30)
entry_NamHoc.grid(row=3, column=1, pady=10, padx=10)

# Mã lớp
label_MaLop = ttk.Label(input_frame, text="Mã lớp:")
label_MaLop.grid(row=4, column=0, sticky=E, padx=10, pady=10)
entry_MaLop = ttk.Entry(input_frame, width=30)
entry_MaLop.grid(row=4, column=1, pady=10, padx=10)

button_assign_schedule = ttk.Button(main_frame, text="Phân Công Lịch Giảng", command=loaddulieuvaodatabase)
button_assign_schedule.grid(row=1, column=1, pady=20, padx=10, sticky=E)

button_exit = ttk.Button(main_frame, text="Thoát", command=exit_app)
button_exit.grid(row=1, column=0, pady=20, padx=10, sticky=W)

window.mainloop()
