from datetime import datetime
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
import re
import openpyxl


chinhSua_GV = Tk()
chinhSua_GV.title("Quản lý giảng viên")

# Kết nối DB
conn = sqlite3.connect("qlgv.db")
cur = conn.cursor()

def manHinh(event):
    chinhSua_GV.attributes("-fullscreen", not chinhSua_GV.attributes("-fullscreen"))
    chinhSua_GV.geometry("1280x720")

def ht_bang():
    # Xóa dữ liệu cũ trong Treeview
    for row in bang.get_children():
        bang.delete(row)

    # Truy vấn dữ liệu từ CSDL
    cur.execute("SELECT * FROM GiangVien")
    rows = cur.fetchall()

    # Điền dữ liệu vào Treeview
    for row in rows:
        bang.insert("", END, values=row)


def timKiem(event):
    tk = et_tk.get()  # Lấy giá trị từ Entry

    if tk == "":
        ht_bang()  # Hiển thị bảng khi không nhập gì
    else:
        # Xóa dữ liệu cũ trong Treeview
        for row in bang.get_children():
            bang.delete(row)

        # Tạo lệnh SQL để tìm kiếm
        sql = """SELECT * FROM GiangVien 
                WHERE MaGV LIKE ? OR HoTen LIKE ? OR NgaySinh LIKE ? OR GioiTinh LIKE ? OR 
                DiaChi LIKE ? OR Email LIKE ? OR SoDienThoai LIKE ?
            """

        # Tạo tuple (bất biến) chứa các giá trị tìm kiếm cho từng cột
        param = tuple(f"%{tk}%" for _ in range(7))

        # Truy vấn dữ liệu từ CSDL
        cur.execute(sql, param)

        # Lấy giá trị của tất cả các hàng
        rows = cur.fetchall()

        if rows:
            # Điền dữ liệu vào Treeview
            for row in rows:
                bang.insert("", "end", values=row)
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy kết quả")
            et_tk.delete(0, END) # Xóa dữ liệu Entry tìm kiếm
            ht_bang() # Hiển thị lại bảng

def them():
    # Lấy dữ liệu từ các Entry và Radiobutton
    mgv = et_mgv.get()
    ten = et_tenGV.get()
    nSinh = et_ns.get()
    gTinh = gt.get()
    dC = et_dc.get()
    mail = et_mail.get()
    sdt = et_SDT.get()

    hoi = messagebox.askquestion("Thông báo", "Bạn có chắc muốn thêm không?", type=messagebox.YESNO)
    if hoi == "no":
        return

    # Kiểm tra các trường thông tin có được điền đầy đủ không
    if mgv == '' or ten == '' or nSinh == '' or gTinh == '' or dC == '' or mail == '' or sdt == '':
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return

    mess = ""

    # Kiểm tra ngày sinh định dạng 'yyyy-mm-dd'
    try:
        datetime.strptime(nSinh, '%Y-%m-%d')
    except ValueError:
        mess += "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng yyyy-mm-dd.\n"

    # Kiểm tra định dạng email
    kt_Mail = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(kt_Mail, mail):
        mess += "Địa chỉ email không hợp lệ.\n"

    # Kiểm tra định dạng số điện thoại
    if not sdt.isdigit() or len(sdt) < 10 or len(sdt) > 15:
        mess += "Số điện thoại không hợp lệ.\n"

    # Thông báo kiểm tra
    if mess != '':
        messagebox.showerror("Lỗi", mess)
        return

    try:
        # Kiểm tra xem Mã GV đã tồn tại chưa
        cur.execute("SELECT * FROM GiangVien WHERE MaGV=?", (mgv,))
        row = cur.fetchone()
        if row:
            messagebox.showerror("Lỗi", f"Mã GV: '{mgv}' đã tồn tại. Vui lòng nhập Mã GV khác.")
            return

        # Thực hiện câu lệnh SQL để thêm dữ liệu vào CSDL
        cur.execute(
            """INSERT INTO GiangVien (MaGV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (mgv, ten, nSinh, gTinh, dC, mail, sdt))

        # Lưu thay đổi và commit vào CSDL
        conn.commit()

        # Hiển thị thông báo khi thêm thành công
        messagebox.showinfo("Thông báo", "Thêm giảng viên thành công")

        # Cập nhật lại bảng hiển thị dữ liệu
        ht_bang()

        # Xóa dữ liệu trong các Entry sau khi thêm thành công
        et_mgv.delete(0, END)
        et_tenGV.delete(0, END)
        et_ns.delete(0, END)
        gt.set('')  # Reset Radiobutton
        et_dc.delete(0, END)
        et_mail.delete(0, END)
        et_SDT.delete(0, END)

    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")


def sua():
    # Lấy dữ liệu từ các Entry và Radiobutton
    mgv = et_mgv.get()
    ten = et_tenGV.get()
    nSinh = et_ns.get()
    gTinh = gt.get()
    dC = et_dc.get()
    mail = et_mail.get()
    sdt = et_SDT.get()

    # Kiểm tra xem người dùng đã chọn giảng viên nào để sửa chưa
    chon = bang.focus()  # Lấy item được chọn trong Treeview
    if not chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn giảng viên cần sửa trong danh sách.")
        return

    # Lấy thông tin của giảng viên được chọn từ Treeview
    item = bang.item(chon, 'values')
    mgv_cu = item[0]  # Mã GV cũ của giảng viên

    hoi = messagebox.askquestion("Thông báo", "Bạn có chắc muốn sửa không?", type=messagebox.YESNO)
    if hoi == "no":
        return

    # Kiểm tra xem người dùng đã nhập thông tin cần sửa chưa
    if not (mgv or ten or nSinh or gTinh or dC or mail or sdt):
        messagebox.showerror("Lỗi", "Vui lòng nhập ít nhất một trường thông tin cần sửa.")
        return

    mess = ""

    # Kiểm tra ngày sinh định dạng 'yyyy-mm-dd'
    try:
        datetime.strptime(nSinh, '%Y-%m-%d')
    except ValueError:
        mess += "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng yyyy-mm-dd.\n"

    # Kiểm tra định dạng email
    kt_Mail = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(kt_Mail, mail):
        mess += "Địa chỉ email không hợp lệ.\n"

    # Kiểm tra định dạng số điện thoại
    if not sdt.isdigit() or len(sdt) < 10 or len(sdt) > 15:
        mess += "Số điện thoại không hợp lệ.\n"

    # Thông báo kiểm tra
    if mess != '':
        messagebox.showerror("Lỗi", mess)
        return

    try:
        # Bắt đầu xây dựng câu lệnh SQL để cập nhật
        sql = "UPDATE GiangVien SET "
        lst = []

        # Kiểm tra và thêm các cột cần cập nhật vào câu lệnh SQL
        if mgv:
            sql += "MaGV = ?, "
            lst.append(mgv)
        if ten:
            sql += "HoTen = ?, "
            lst.append(ten)
        if nSinh:
            sql += "NgaySinh = ?, "
            lst.append(nSinh)
        if gTinh:
            sql += "GioiTinh = ?, "
            lst.append(gTinh)
        if dC:
            sql += "DiaChi = ?, "
            lst.append(dC)
        if mail:
            sql += "Email = ?, "
            lst.append(mail)
        if sdt:
            sql += "SoDienThoai = ?, "
            lst.append(sdt)

        # Xóa ký tự ", " cuối cùng của câu lệnh SQL
        sql = sql.rstrip(", ")

        # Thêm điều kiện WHERE để chỉ cập nhật dòng có MaGV tương ứng
        sql += " WHERE MaGV = ?"
        lst.append(mgv_cu)

        # Thực hiện câu lệnh SQL để cập nhật dữ liệu vào CSDL
        cur.execute(sql, lst)

        # Lưu thay đổi và commit vào CSDL
        conn.commit()

        # Hiển thị thông báo khi sửa thành công
        messagebox.showinfo("Thông báo", "Sửa thông tin giảng viên thành công")

        # Cập nhật lại bảng hiển thị dữ liệu
        ht_bang()

        # Xóa dữ liệu trong các Entry sau khi sửa thành công
        et_mgv.delete(0, END)
        et_tenGV.delete(0, END)
        et_ns.delete(0, END)
        gt.set('')  # Reset Radiobutton
        et_dc.delete(0, END)
        et_mail.delete(0, END)
        et_SDT.delete(0, END)

    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")


def xoa():
    # Kiểm tra xem người dùng đã chọn giảng viên nào để sửa chưa
    chon = bang.focus()  # Lấy item được chọn trong Treeview
    if not chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn giảng viên cần xóa trong danh sách.")
        return

    # Lấy thông tin của giảng viên được chọn từ Treeview
    item = bang.item(chon, 'values')
    mgv = item[0]  # Mã GV của giảng viên

    try:
        hoiXoa = messagebox.askquestion("Chú ý", f"Bạn có chắc xóa giảng viên {mgv}", type=messagebox.YESNO)
        if hoiXoa == 'yes':
            # Xóa dữ liệu trong SQL
            cur.execute("DELETE FROM GiangVien WHERE MaGV=?", (mgv,))
            conn.commit()

            messagebox.showinfo("Thông báo", "Xóa thành công")

            # Hiển thị lại bảng
            ht_bang()
    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")


def xuat_excel():
    try:
        # Truy vấn tất cả dữ liệu từ bảng GiangVien
        cur.execute("SELECT * FROM GiangVien")
        rows = cur.fetchall()

        # Tạo một workbook và worksheet mới
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "GiangVien"

        # Thiết lập tiêu đề cột
        cot = ["MaGV", "HoTen", "NgaySinh", "GioiTinh", "DiaChi", "Email", "SoDienThoai"]
        ws.append(cot)

        # Thêm dữ liệu vào worksheet
        for row in rows:
            ws.append(row)

        # Lưu file Excel
        wb.save("DanhSachGiangVien.xlsx")

        # Hiển thị thông báo khi xuất thành công
        messagebox.showinfo("Thông báo", "Xuất file Excel thành công")

    except Exception as e:
        # Hiển thị thông báo khi có lỗi xảy ra
        messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")


## Tạo form
#Label, Entry

tieuDe = Label(chinhSua_GV, text="Quản lý giảng viên", font=("Arial", 24, 'bold'), justify="center")
tieuDe.place(x=600, y=20)

muc1 = Label(chinhSua_GV, text="Nhập thông tin:", font=("Arial", 18, 'bold'))
muc1.place(x=40, y=140)

lb_tk = Label(chinhSua_GV, text="Tìm kiếm: ", font=("Arial", 12))
lb_tk.place(x=780, y=155, width=200, height=30)
et_tk = Entry(chinhSua_GV, bd=2, relief=SOLID)
et_tk.bind("<KeyRelease>", timKiem)
et_tk.place(x=930, y=155, width=250, height=30)

lb_mgv = Label(chinhSua_GV, text="Mã GV: ", font=("Arial", 12))
lb_mgv.place(x=20, y=190, width=200, height=30)
et_mgv = Entry(chinhSua_GV, font=("Arial", 12))
et_mgv.place(x=230, y=190, width=250, height=30)

lb_tenGV = Label(chinhSua_GV, text="Tên GV: ", font=("Arial", 12))
lb_tenGV.place(x=20, y=230, width=200, height=30)
et_tenGV = Entry(chinhSua_GV, font=("Arial", 12))
et_tenGV.place(x=230, y=230, width=250, height=30)

lb_ns = Label(chinhSua_GV, text="Ngày sinh: ", font=("Arial", 12))
lb_ns.place(x=20, y=270, width=200, height=30)
et_ns = Entry(chinhSua_GV, font=("Arial", 12))
et_ns.place(x=230, y=270, width=250, height=30)

lb_gt = Label(chinhSua_GV, text="Giới tính: ", font=("Arial", 12))
lb_gt.place(x=20, y=310, width=200, height=30)
gt = StringVar()
Radiobutton(chinhSua_GV, text="Nam", padx=5, variable=gt, value='Nam', font=("Arial", 12)).place(x=230, y=310)
Radiobutton(chinhSua_GV, text="Nữ", padx =10, variable=gt, value='Nữ', font=("Arial", 12)).place(x=320, y=310)
Radiobutton(chinhSua_GV, text="Khác", padx=15, variable=gt, value='Khác', font=("Arial", 12)).place(x=400, y=310)

lb_dc = Label(chinhSua_GV, text="Địa chỉ: ", font=("Arial", 12))
lb_dc.place(x=20, y=350, width=200, height=30)
et_dc = Entry(chinhSua_GV, font=("Arial", 12))
et_dc.place(x=230, y=350, width=250, height=30)

lb_mail = Label(chinhSua_GV, text="Email: ", font=("Arial", 12))
lb_mail.place(x=20, y=390, width=200, height=30)
et_mail = Entry(chinhSua_GV, font=("Arial", 12))
et_mail.place(x=230, y=390, width=250, height=30)

lb_SDT = Label(chinhSua_GV, text="SĐT: ", font=("Arial", 12))
lb_SDT.place(x=20, y=430, width=200, height=30)
et_SDT = Entry(chinhSua_GV, font=("Arial", 12))
et_SDT.place(x=230, y=430, width=250, height=30)

# Buttons

btn_add = Button(chinhSua_GV, text="Thêm", width=15, font=("Arial", 12, 'bold'), command=them)
btn_add.place(x=20, y=480, width=150, height=40)

btn_upd = Button(chinhSua_GV, text="Sửa", width=15, font=("Arial", 12, 'bold'), command=sua)
btn_upd.place(x=200, y=480, width=150, height=40)

btn_del = Button(chinhSua_GV, text="Xóa", width=15, font=("Arial", 12, 'bold'), command=xoa)
btn_del.place(x=380, y=480, width=150, height=40)

btn_xuatEx = Button(chinhSua_GV, text="Xuất Excel", width=15, font=("Arial", 12, 'bold'), command=xuat_excel)
btn_xuatEx.place(x=20, y=540, width=150, height=40)

btn_thoat = Button(chinhSua_GV, text="Thoát", width=15, font=("Arial", 12, 'bold'), command=exit)
btn_thoat.place(x=380, y=540, width=150, height=40)

# Treeview để hiển thị dữ liệu dưới dạng bảng
bang = ttk.Treeview(chinhSua_GV, columns=("MGV", "TenGV", "NgaySinh", "GioiTinh", "DiaChi", "Email", "SDT"), show="headings")
bang.place(x=600, y=200, width=900, height=380)

# Đặt tên cho các cột
bang.heading("MGV", text="Mã GV")
bang.heading("TenGV", text="Tên GV")
bang.heading("NgaySinh", text="Ngày sinh")
bang.heading("GioiTinh", text="Giới tính")
bang.heading("DiaChi", text="Địa chỉ")
bang.heading("Email", text="Email")
bang.heading("SDT", text="SĐT")

# Đặt kích thước ô
bang.column("MGV", width=50)
bang.column("TenGV", width=120)
bang.column("NgaySinh", width=80)
bang.column("GioiTinh", width=80)
bang.column("DiaChi", width=200)
bang.column("Email", width=200)
bang.column("SDT", width=100)

# Hiển thị dữ liệu vào bảng
ht_bang()

# Bật/tắt toàn màn hình
chinhSua_GV.bind("<Escape>", manHinh)
chinhSua_GV.attributes("-fullscreen", True)

chinhSua_GV.mainloop()