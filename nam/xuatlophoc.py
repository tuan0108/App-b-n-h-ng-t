import sqlite3
import pandas as pd


def export_table_to_excel(db_path, excel_path):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect(db_path)

    # Đọc dữ liệu từ bảng vào DataFrame của pandas
    query = f"""SELECT sv.MaSV, sv.HoTen, sv.NgaySinh, sv.GioiTinh, sv.DiaChi, sv.Email, sv.SoDienThoai, l.TenLop
    FROM SinhVien sv
    JOIN Lop l ON sv.MaLop = l.MaLop"""
    df = pd.read_sql_query(query, conn)

    # Đóng kết nối cơ sở dữ liệu
    conn.close()

    # Xuất DataFrame thành file Excel
    df.to_excel(excel_path, index=False)


# Sử dụng hàm để xuất dữ liệu
db_path = 'qlgv.db'  # Đường dẫn tới file cơ sở dữ liệu SQLiteơ
excel_path = 'lophoc.xlsx'  # Đường dẫn tới file Excel đầu ra

export_table_to_excel(db_path, excel_path)
