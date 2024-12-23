from tkinter import *
import sqlite3
from tkinter import messagebox, ttk


main_GV = Tk()
main_GV.title("Giảng viên")

# Kết nối DB
conn = sqlite3.connect("qlgv.db")
cur = conn.cursor()

def manHinh(event):
    main_GV.attributes("-fullscreen", not main_GV.attributes("-fullscreen"))
    main_GV.geometry("1280x720")


def ht_infor():
    try:
        # Xóa dữ liệu cũ trong Treeview (nếu có)
        for i in bang.get_children():
            bang.delete(i)


        # Lấy dữ liệu từ database
        cur.execute("SELECT * FROM GiangVien WHERE MaGV = ?", (ten_ht,))
        tTin = cur.fetchone()

        # Cấu hình Treeview
        bang.config(columns=["c1", "c2", "c3", "c4"], show="headings")
        bang.place(x=400, y=150, width=600, height=400)

        # Đặt kích thước ô
        bang.column("#0", width=0)
        bang.column("c1", width=100)
        bang.column("c2", width=200)
        bang.column("c3", width=100)
        bang.column("c4", width=200)

        data = [
            ("MaGV:", tTin[0], "Địa chỉ:", tTin[4]),
            ("", "", "", ""),
            ("", "", "", ""),
            ("Họ tên:", tTin[1], "Email:", tTin[5]),
            ("", "", "", ""),
            ("", "", "", ""),
            ("Ngày sinh:", tTin[2], "SĐT:", tTin[6]),
            ("", "", "", ""),
            ("", "", "", ""),
            ("Giới tính:", tTin[3], "", "")
        ]

        # Hiển thị dữ liệu trong Treeview
        for i in data:
            bang.insert("", "end", values=i)

    except sqlite3.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi: {e}")

def ht_phanC():
    try:
        # Xóa dữ liệu cũ trong Treeview (nếu có)
        for i in bang.get_children():
            bang.delete(i)

        # Cấu hình Treeview
        bang.config(columns=["mapc", "hp", "hocKy", "nam", "lop"], show='headings')
        bang.heading("mapc", text="MaPC")
        bang.heading("hp", text="Học phần")
        bang.heading("hocKy", text="Học kỳ")
        bang.heading("nam", text="Năm học")
        bang.heading("lop", text="Lớp")
        bang.place(x=400, y=150, width=600, height=400)

        # Đặt kích thước ô
        bang.column("mapc", width=30)
        bang.column("hp", width=200)
        bang.column("hocKy", width=50)
        bang.column("nam", width=100)
        bang.column("lop", width=100)

        # Lấy dữ liệu từ database
        cur.execute(
            """SELECT PhanCong.MaPC, HocPhan.TenHP, PhanCong.HocKy, PhanCong.NamHoc, Lop.TenLop 
                FROM PhanCong, HocPhan, Lop
                WHERE PhanCong.MaHP = HocPhan.MaHP AND PhanCong.MaLop = Lop.MaLop AND PhanCOng.MaGV = ?
                """, (ten_ht, ))
        rows = cur.fetchall()

        # Hiển thị dữ liệu trong Treeview
        for row in rows:
            bang.insert("", "end", values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi: {e}")

def ht_danhGia():
    try:
        # Xóa dữ liệu cũ trong Treeview (nếu có)
        for i in bang.get_children():
            bang.delete(i)

        # Cấu hình Treeview
        bang.config(columns=["madg", "noidung", "diem", "ngay"], show='headings')
        bang.heading("madg", text="MaDG")
        bang.heading("noidung", text="Nội dung")
        bang.heading("diem", text="Điểm số")
        bang.heading("ngay", text="Ngày đánh giá")
        bang.place(x=400, y=150, width=600, height=400)

        # Đặt kích thước ô
        bang.column("madg", width=30)
        bang.column("noidung", width=200)
        bang.column("diem", width=50)
        bang.column("ngay", width=100)

        # Lấy dữ liệu từ database
        cur.execute(
            """SELECT MaDG, NoiDung, DiemSo, NgayDanhGia 
                FROM DanhGia 
                WHERE MaGV = ? """, (ten_ht, ))
        rows = cur.fetchall()

        # Hiển thị dữ liệu trong Treeview
        for row in rows:
            bang.insert("", "end", values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Lỗi", f"Lỗi: {e}")




lb_GV = Label(main_GV, font=("Arial", 18, 'bold'), bd=2, relief=SOLID)
lb_GV.place(x=40, y=40, width=250, height=40)

btn_info = Button(main_GV, text="Thông tin", width=15, font=("Arial", 12, 'bold'), command=ht_infor)
btn_info.place(x=50, y=150, width=200, height=40)

btn_pC = Button(main_GV, text="Phân công", width=15, font=("Arial", 12, 'bold'), command=ht_phanC)
btn_pC.place(x=50, y=200, width=200, height=40)

btn_dg = Button(main_GV, text="Xem đánh giá", width=15, font=("Arial", 12, 'bold'), command=ht_danhGia)
btn_dg.place(x=50, y=250, width=200, height=40)

lb_tt = Label(main_GV, font=("Arial", 12), justify="left")

btn_dangX = Button(main_GV, text="Đăng xuất", width=15, font=("Arial", 12, 'bold'), command=exit)
btn_dangX.place(x=50, y=500, width=200, height=40)

# Tạo bảng
bang = ttk.Treeview(main_GV)

# Hiển thị tên
with open('HienThi.txt', 'r') as f:
    ten_ht = f.read().strip()
    # Lấy dữ liệu từ database
    cur.execute(
        """SELECT Hoten 
            FROM GiangVien 
            WHERE MaGV = ? """, (ten_ht, ))
    ten = cur.fetchone()
    ten = ten[0]
    lb_GV.config(text=ten)

# Bật/tắt toàn màn hình
main_GV.bind("<Escape>", manHinh)
main_GV.attributes("-fullscreen", True)

main_GV.mainloop()
