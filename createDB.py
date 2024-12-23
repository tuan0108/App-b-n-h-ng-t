import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect('qlgv.db')
cur = conn.cursor()

# Tạo bảng Giảng viên
cur.execute('''
CREATE TABLE IF NOT EXISTS GiangVien (
    MaGV TEXT PRIMARY KEY,
    HoTen TEXT,
    NgaySinh DATE,
    GioiTinh TEXT,
    DiaChi TEXT,
    Email TEXT,
    SoDienThoai TEXT
)
''')

# Tạo bảng Học phần
cur.execute('''
CREATE TABLE IF NOT EXISTS HocPhan (
    MaHP TEXT PRIMARY KEY,
    TenHP TEXT,
    SoTinChi INTEGER
)
''')

# Tạo bảng Phân công giảng dạy
cur.execute('''
CREATE TABLE IF NOT EXISTS PhanCong (
    MaPC INTEGER PRIMARY KEY AUTOINCREMENT,
    MaGV TEXT,
    MaHP TEXT,
    HocKy TEXT,
    NamHoc TEXT,
    MaLop TEXT,
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV) ON DELETE SET NULL,
    FOREIGN KEY (MaHP) REFERENCES HocPhan(MaHP) ON DELETE SET NULL,
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop) ON DELETE SET NULL
)
''')

# Tạo bảng Sinh viên
cur.execute('''
CREATE TABLE IF NOT EXISTS SinhVien (
    MaSV TEXT PRIMARY KEY,
    HoTen TEXT,
    NgaySinh DATE,
    GioiTinh TEXT,
    DiaChi TEXT,
    Email TEXT,
    SoDienThoai TEXT,
    MaLop TEXT,
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop) ON DELETE SET NULL
)
''')

# Tạo bảng Đánh giá giảng viên
cur.execute('''
CREATE TABLE IF NOT EXISTS DanhGia (
    MaDG INTEGER PRIMARY KEY AUTOINCREMENT,
    MaGV TEXT,
    MaSV TEXT,
    NoiDung TEXT,
    DiemSo INTEGER CHECK (DiemSo >= 1 AND DiemSo <= 10),
    NgayDanhGia DATE,
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV) ON DELETE SET NULL,
    FOREIGN KEY (MaSV) REFERENCES SinhVien(MaSV) ON DELETE SET NULL
)
''')

# Tạo bảng Tài khoản
cur.execute('''
CREATE TABLE IF NOT EXISTS TaiKhoan (
    TenDangNhap TEXT PRIMARY KEY,
    MatKhau TEXT,
    VaiTro TEXT,
    MaNguoiDung TEXT,
    FOREIGN KEY (MaNguoiDung) REFERENCES GiangVien(MaGV) ON DELETE CASCADE,
    FOREIGN KEY (MaNguoiDung) REFERENCES SinhVien(MaSV) ON DELETE CASCADE
)
''')

# Tạo bảng Lớp
cur.execute('''
CREATE TABLE IF NOT EXISTS Lop (
    MaLop TEXT PRIMARY KEY,
    TenLop TEXT,
    MaGVPT TEXT,
    FOREIGN KEY (MaGVPT) REFERENCES GiangVien(MaGV) ON DELETE SET NULL
)
''')

# Thêm dữ liệu vào bảng Giảng viên
giang_vien_data = [
    ('GV001', 'Nguyễn Văn A', '1980-01-01', 'Nam', 'Hà Nội', 'nguyenvana@gmail.com', '0123456789'),
    ('GV002', 'Trần Thị B', '1982-02-02', 'Nữ', 'Hải Phòng', 'tranthib@gmail.com', '0987654321'),
    ('GV003', 'Lê Văn C', '1983-03-03', 'Nam', 'Đà Nẵng', 'levanc@gmail.com', '0912345678'),
    ('GV004', 'Phạm Thị D', '1984-04-04', 'Nữ', 'Huế', 'phamthid@gmail.com', '0923456789'),
    ('GV005', 'Ngô Văn E', '1985-05-05', 'Nam', 'Quảng Ninh', 'ngovane@gmail.com', '0934567890'),
    ('GV006', 'Đỗ Thị F', '1986-06-06', 'Nữ', 'Nha Trang', 'dothif@gmail.com', '0945678901'),
    ('GV007', 'Vũ Văn G', '1987-07-07', 'Nam', 'Hải Dương', 'vuvang@gmail.com', '0956789012'),
    ('GV008', 'Bùi Thị H', '1988-08-08', 'Nữ', 'Cần Thơ', 'buithih@gmail.com', '0967890123'),
    ('GV009', 'Trương Văn I', '1989-09-09', 'Nam', 'Nam Định', 'truongvani@gmail.com', '0978901234'),
    ('GV010', 'Hoàng Thị J', '1990-10-10', 'Nữ', 'Vĩnh Phúc', 'hoangthij@gmail.com', '0989012345'),
    ('GV011', 'Phùng Văn K', '1991-11-11', 'Nam', 'Thái Nguyên', 'phungvank@gmail.com', '0990123456'),
    ('GV012', 'Trịnh Thị L', '1992-12-12', 'Nữ', 'Thanh Hóa', 'trinhthil@gmail.com', '0901234567')
]

cur.executemany("INSERT INTO GiangVien (MaGV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai) VALUES (?, ?, ?, ?, ?, ?, ?)", giang_vien_data)

# Thêm dữ liệu vào bảng Học phần
hoc_phan_data = [
    ('HP001', 'Toán Cao Cấp', 3),
    ('HP002', 'Lý Thuyết Đồ Thị', 2),
    ('HP003', 'Cơ Sở Dữ Liệu', 3),
    ('HP004', 'Cấu Trúc Dữ Liệu', 3),
    ('HP005', 'Mạng Máy Tính', 2),
    ('HP006', 'Hệ Điều Hành', 3),
    ('HP007', 'Lập Trình Hướng Đối Tượng', 4),
    ('HP008', 'Phân Tích Thiết Kế Hệ Thống', 3),
    ('HP009', 'An Toàn Thông Tin', 2),
    ('HP010', 'Lập Trình Web', 3),
    ('HP011', 'Trí Tuệ Nhân Tạo', 4),
    ('HP012', 'Kỹ Thuật Số', 3)
]

cur.executemany("INSERT INTO HocPhan (MaHP, TenHP, SoTinChi) VALUES (?, ?, ?)", hoc_phan_data)

# Thêm dữ liệu vào bảng Lớp
lop_data = [
    ('L001', 'CNTT1', 'GV001'),
    ('L002', 'CNTT2', 'GV002'),
    ('L003', 'CNTT3', 'GV003'),
    ('L004', 'CNTT4', 'GV004'),
    ('L005', 'CNTT5', 'GV005'),
    ('L006', 'CNTT6', 'GV006'),
    ('L007', 'CNTT7', 'GV007'),
    ('L008', 'CNTT8', 'GV008'),
    ('L009', 'CNTT9', 'GV009'),
    ('L010', 'CNTT10', 'GV010'),
    ('L011', 'CNTT11', 'GV011'),
    ('L012', 'CNTT12', 'GV012')
]

cur.executemany("INSERT INTO Lop (MaLop, TenLop, MaGVPT) VALUES (?, ?, ?)", lop_data)

# Thêm dữ liệu vào bảng Sinh viên
sinh_vien_data = [
    ('SV001', 'Lê Văn C', '2000-03-03', 'Nam', 'Đà Nẵng', 'levanc@gmail.com', '0901234567', 'L001'),
    ('SV002', 'Nguyễn Thị D', '2000-04-04', 'Nữ', 'Hà Nội', 'nguyenthid@gmail.com', '0912345678', 'L002'),
    ('SV003', 'Phạm Văn E', '2000-05-05', 'Nam', 'Hải Phòng', 'phamvane@gmail.com', '0923456789', 'L003'),
    ('SV004', 'Trần Thị F', '2000-06-06', 'Nữ', 'Huế', 'tranthif@gmail.com', '0934567890', 'L004'),
    ('SV005', 'Đỗ Văn G', '2000-07-07', 'Nam', 'Nha Trang', 'dovang@gmail.com', '0945678901', 'L005'),
    ('SV006', 'Ngô Thị H', '2000-08-08', 'Nữ', 'Quảng Ninh', 'ngothih@gmail.com', '0956789012', 'L006'),
    ('SV007', 'Vũ Văn I', '2000-09-09', 'Nam', 'Hải Dương', 'vuvani@gmail.com', '0967890123', 'L007'),
    ('SV008', 'Bùi Thị J', '2000-10-10', 'Nữ', 'Cần Thơ', 'buithij@gmail.com', '0978901234', 'L008'),
    ('SV009', 'Trương Văn K', '2000-11-11', 'Nam', 'Nam Định', 'truongvank@gmail.com', '0989012345', 'L009'),
    ('SV010', 'Hoàng Thị L', '2000-12-12', 'Nữ', 'Vĩnh Phúc', 'hoangthil@gmail.com', '0990123456', 'L010'),
    ('SV011', 'Phùng Văn M', '2001-01-01', 'Nam', 'Thái Nguyên', 'phungvanm@gmail.com', '0900123456', 'L011'),
    ('SV012', 'Trịnh Thị N', '2001-02-02', 'Nữ', 'Thanh Hóa', 'trinhthin@gmail.com', '0910123456', 'L012')
]

cur.executemany("INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai, MaLop) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", sinh_vien_data)

# Thêm dữ liệu vào bảng Phân công giảng dạy
phan_cong_data = [
    (1, 'GV001', 'HP001', '2021-1', '2021-2022', 'L001'),
    (2, 'GV002', 'HP002', '2021-1', '2021-2022', 'L002'),
    (3, 'GV003', 'HP003', '2021-1', '2021-2022', 'L003'),
    (4, 'GV004', 'HP004', '2021-1', '2021-2022', 'L004'),
    (5, 'GV005', 'HP005', '2021-1', '2021-2022', 'L005'),
    (6, 'GV006', 'HP006', '2021-1', '2021-2022', 'L006'),
    (7, 'GV007', 'HP007', '2021-1', '2021-2022', 'L007'),
    (8, 'GV008', 'HP008', '2021-1', '2021-2022', 'L008'),
    (9, 'GV009', 'HP009', '2021-1', '2021-2022', 'L009'),
    (10, 'GV010', 'HP010', '2021-1', '2021-2022', 'L010'),
    (11, 'GV011', 'HP011', '2021-1', '2021-2022', 'L011'),
    (12, 'GV012', 'HP012', '2021-1', '2021-2022', 'L012')
]

cur.executemany("INSERT INTO PhanCong (MaPC, MaGV, MaHP, HocKy, NamHoc, MaLop) VALUES (?, ?, ?, ?, ?, ?)", phan_cong_data)

# Thêm dữ liệu vào bảng Đánh giá giảng viên
danh_gia_data = [
    (1, 'GV001', 'SV001', 'Giảng viên rất nhiệt tình và có kiến thức sâu rộng.', 9, '2022-01-01'),
    (2, 'GV002', 'SV002', 'Giảng viên truyền đạt tốt và dễ hiểu.', 8, '2022-01-02'),
    (3, 'GV003', 'SV003', 'Bài giảng sinh động và hấp dẫn.', 10, '2022-01-03'),
    (4, 'GV004', 'SV004', 'Giảng viên hơi khó tính.', 7, '2022-01-04'),
    (5, 'GV005', 'SV005', 'Giảng viên rất tận tâm.', 9, '2022-01-05'),
    (6, 'GV006', 'SV006', 'Giảng viên thân thiện và dễ gần.', 8, '2022-01-06'),
    (7, 'GV007', 'SV007', 'Giảng viên có phong cách giảng dạy rất độc đáo.', 9, '2022-01-07'),
    (8, 'GV008', 'SV008', 'Giảng viên yêu cầu cao và khó tính.', 6, '2022-01-08'),
    (9, 'GV009', 'SV009', 'Giảng viên rất hiểu tâm lý sinh viên.', 10, '2022-01-09'),
    (10, 'GV010', 'SV010', 'Giảng viên luôn hỗ trợ sinh viên hết mình.', 9, '2022-01-10'),
    (11, 'GV011', 'SV011', 'Giảng viên có cách giảng dạy hơi nhàm chán.', 5, '2022-01-11'),
    (12, 'GV012', 'SV012', 'Giảng viên có kiến thức chuyên môn rất tốt.', 8, '2022-01-12')
]

cur.executemany("INSERT INTO DanhGia (MaDG, MaGV, MaSV, NoiDung, DiemSo, NgayDanhGia) VALUES (?, ?, ?, ?, ?, ?)", danh_gia_data)

# Thêm dữ liệu vào bảng Tài khoản
tai_khoan_data = [
    ('admin', 'admin', 'Quản trị viên', ''),
    ('GV001', 'abc1', 'Giảng viên', 'GV001'),
    ('GV002', 'abc1', 'Giảng viên', 'GV002'),
    ('GV003', 'abc1', 'Giảng viên', 'GV003'),
    ('GV004', 'abc1', 'Giảng viên', 'GV004'),
    ('GV005', 'abc1', 'Giảng viên', 'GV005'),
    ('GV006', 'abc1', 'Giảng viên', 'GV006'),
    ('GV007', 'abc1', 'Giảng viên', 'GV007'),
    ('GV008', 'abc1', 'Giảng viên', 'GV008'),
    ('GV009', 'abc1', 'Giảng viên', 'GV009'),
    ('GV010', 'abc1', 'Giảng viên', 'GV010'),
    ('GV011', 'abc1', 'Giảng viên', 'GV011'),
    ('GV012', 'abc1', 'Giảng viên', 'GV012'),
    ('SV001', 'abc1', 'Sinh viên', 'SV001'),
    ('SV002', 'abc1', 'Sinh viên', 'SV002'),
    ('SV003', 'abc1', 'Sinh viên', 'SV003'),
    ('SV004', 'abc1', 'Sinh viên', 'SV004'),
    ('SV005', 'abc1', 'Sinh viên', 'SV005'),
    ('SV006', 'abc1', 'Sinh viên', 'SV006'),
    ('SV007', 'abc1', 'Sinh viên', 'SV007'),
    ('SV008', 'abc1', 'Sinh viên', 'SV008'),
    ('SV009', 'abc1', 'Sinh viên', 'SV009'),
    ('SV010', 'abc1', 'Sinh viên', 'SV010'),
    ('SV011', 'abc1', 'Sinh viên', 'SV011'),
    ('SV012', 'abc1', 'Sinh viên', 'SV012')
]

cur.executemany("INSERT INTO TaiKhoan (TenDangNhap, MatKhau, VaiTro, MaNguoiDung) VALUES (?, ?, ?, ?)", tai_khoan_data)


conn.commit()
conn.close()
