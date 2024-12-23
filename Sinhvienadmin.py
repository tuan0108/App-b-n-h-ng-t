from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 381, 451))
        self.widget.setObjectName("widget")

        self.label1 = QtWidgets.QLabel(parent=self.widget)
        self.label1.setGeometry(QtCore.QRect(60, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.label_maSV = QtWidgets.QLabel(parent=self.widget)
        self.label_maSV.setGeometry(QtCore.QRect(30, 50, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_maSV.setFont(font)
        self.label_maSV.setObjectName("label_maSV")

        self.label_name = QtWidgets.QLabel(parent=self.widget)
        self.label_name.setGeometry(QtCore.QRect(30, 80, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")

        self.label_ngsinh = QtWidgets.QLabel(parent=self.widget)
        self.label_ngsinh.setGeometry(QtCore.QRect(30, 110, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_ngsinh.setFont(font)
        self.label_ngsinh.setObjectName("label_ngsinh")

        self.label_gioitinh = QtWidgets.QLabel(parent=self.widget)
        self.label_gioitinh.setGeometry(QtCore.QRect(30, 140, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_gioitinh.setFont(font)
        self.label_gioitinh.setObjectName("label_gioitinh")

        self.label_diachi = QtWidgets.QLabel(parent=self.widget)
        self.label_diachi.setGeometry(QtCore.QRect(30, 170, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_diachi.setFont(font)
        self.label_diachi.setObjectName("label_diachi")

        self.label_email = QtWidgets.QLabel(parent=self.widget)
        self.label_email.setGeometry(QtCore.QRect(30, 200, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")

        self.label_sdt = QtWidgets.QLabel(parent=self.widget)
        self.label_sdt.setGeometry(QtCore.QRect(30, 230, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_sdt.setFont(font)
        self.label_sdt.setObjectName("label_sdt")

        self.label_malop = QtWidgets.QLabel(parent=self.widget)
        self.label_malop.setGeometry(QtCore.QRect(30, 260, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_malop.setFont(font)
        self.label_malop.setObjectName("label_malop")

        self.box_gioitinh = QtWidgets.QComboBox(parent=self.widget)
        self.box_gioitinh.setGeometry(QtCore.QRect(160, 140, 69, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.box_gioitinh.setFont(font)
        self.box_gioitinh.setObjectName("box_gioitinh")
        self.box_gioitinh.addItem("")
        self.box_gioitinh.addItem("")
        self.box_gioitinh.addItem("")

        self.button_them = QtWidgets.QPushButton(parent=self.widget)
        self.button_them.setGeometry(QtCore.QRect(20, 340, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_them.setFont(font)
        self.button_them.setObjectName("button_them")

        self.button_sua = QtWidgets.QPushButton(parent=self.widget)
        self.button_sua.setGeometry(QtCore.QRect(150, 340, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_sua.setFont(font)
        self.button_sua.setObjectName("button_sua")

        self.button_xoa = QtWidgets.QPushButton(parent=self.widget)
        self.button_xoa.setGeometry(QtCore.QRect(270, 340, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_xoa.setFont(font)
        self.button_xoa.setObjectName("button_xoa")

        self.line_masv = QtWidgets.QLineEdit(parent=self.widget)
        self.line_masv.setGeometry(QtCore.QRect(160, 50, 161, 25))
        self.line_masv.setObjectName("line_masv")

        self.line_name = QtWidgets.QLineEdit(parent=self.widget)
        self.line_name.setGeometry(QtCore.QRect(160, 80, 161, 25))
        self.line_name.setObjectName("line_name")

        self.line_ngsinh = QtWidgets.QLineEdit(parent=self.widget)
        self.line_ngsinh.setGeometry(QtCore.QRect(160, 110, 161, 25))
        self.line_ngsinh.setObjectName("line_ngsinh")

        self.line_diachi = QtWidgets.QLineEdit(parent=self.widget)
        self.line_diachi.setGeometry(QtCore.QRect(160, 170, 161, 25))
        self.line_diachi.setObjectName("line_diachi")

        self.line_email = QtWidgets.QLineEdit(parent=self.widget)
        self.line_email.setGeometry(QtCore.QRect(160, 200, 161, 25))
        self.line_email.setObjectName("line_email")

        self.line_sdt = QtWidgets.QLineEdit(parent=self.widget)
        self.line_sdt.setGeometry(QtCore.QRect(160, 230, 161, 25))
        self.line_sdt.setObjectName("line_sdt")

        self.line_malop = QtWidgets.QLineEdit(parent=self.widget)
        self.line_malop.setGeometry(QtCore.QRect(160, 260, 161, 25))
        self.line_malop.setObjectName("line_malop")

        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(400, 70, 911, 41))
        self.widget_2.setObjectName("widget_2")

        self.line_timkiem = QtWidgets.QLineEdit(parent=self.widget_2)
        self.line_timkiem.setGeometry(QtCore.QRect(160, 10, 411, 30))
        self.line_timkiem.setStyleSheet("QLineEdit{\n"
                                        "    padding-left:20px;\n"
                                        "    border:1px solid gray;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "")
        self.line_timkiem.setObjectName("line_timkiem")

        self.button_timkiem = QtWidgets.QPushButton(parent=self.widget_2)
        self.button_timkiem.setGeometry(QtCore.QRect(600, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_timkiem.setFont(font)
        self.button_timkiem.setObjectName("button_timkiem")

        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(400, 120, 921, 361))
        self.widget_3.setObjectName("widget_3")

        self.table_danhsach = QtWidgets.QTableWidget(parent=self.widget_3)
        self.table_danhsach.setGeometry(QtCore.QRect(20, 30, 861, 301))
        self.table_danhsach.setObjectName("table_danhsach")
        self.table_danhsach.setColumnCount(8)
        self.table_danhsach.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_danhsach.setHorizontalHeaderItem(7, item)

        self.label0 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(580, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label0.setFont(font)
        self.label0.setObjectName("label0")

        self.button_thoat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_thoat.setGeometry(QtCore.QRect(1180, 540, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_thoat.setFont(font)
        self.button_thoat.setObjectName("button_thoat")
        self.button_thoat.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Database connection
        self.conn = sqlite3.connect("qlgv.db")
        self.cur = self.conn.cursor()

        # Connect buttons to functions
        self.button_them.clicked.connect(self.add_student)
        self.button_sua.clicked.connect(self.update_student)
        self.button_xoa.clicked.connect(self.delete_student)
        self.button_timkiem.clicked.connect(self.search_student)

        self.load_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Nhập thông tin sinh viên"))
        self.label_maSV.setText(_translate("MainWindow", "Mã sinh viên:"))
        self.label_name.setText(_translate("MainWindow", "Họ tên:"))
        self.label_ngsinh.setText(_translate("MainWindow", "Ngày sinh:"))
        self.label_gioitinh.setText(_translate("MainWindow", "Giới tính:"))
        self.label_diachi.setText(_translate("MainWindow", "Địa chỉ:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_sdt.setText(_translate("MainWindow", "SĐT:"))
        self.label_malop.setText(_translate("MainWindow", "Mã lớp:"))
        self.box_gioitinh.setItemText(0, _translate("MainWindow", "Nam"))
        self.box_gioitinh.setItemText(1, _translate("MainWindow", "Nữ "))
        self.box_gioitinh.setItemText(2, _translate("MainWindow", "Khác"))
        self.button_them.setText(_translate("MainWindow", "Thêm"))
        self.button_sua.setText(_translate("MainWindow", "Sửa "))
        self.button_xoa.setText(_translate("MainWindow", "Xóa"))
        self.line_timkiem.setPlaceholderText(_translate("MainWindow", "Tìm kiếm..."))
        self.button_timkiem.setText(_translate("MainWindow", "Tìm kiếm"))
        item = self.table_danhsach.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Sv"))
        item = self.table_danhsach.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ tên"))
        item = self.table_danhsach.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày sinh"))
        item = self.table_danhsach.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.table_danhsach.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Địa chỉ"))
        item = self.table_danhsach.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table_danhsach.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SĐT"))
        item = self.table_danhsach.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Mã lớp"))
        self.label0.setText(_translate("MainWindow", "Quản lý sinh viên"))
        self.button_thoat.setText(_translate("MainWindow", "Thoát"))

    def load_data(self):
        self.table_danhsach.setRowCount(0)
        self.cur.execute("SELECT * FROM SinhVien")
        rows = self.cur.fetchall()
        for row in rows:
            rowPosition = self.table_danhsach.rowCount()
            self.table_danhsach.insertRow(rowPosition)
            for column, data in enumerate(row):
                self.table_danhsach.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(data)))

    def add_student(self):
        masv = self.line_masv.text()
        hoten = self.line_name.text()
        ngaysinh = self.line_ngsinh.text()
        gioitinh = self.box_gioitinh.currentText()
        diachi = self.line_diachi.text()
        email = self.line_email.text()
        sdt = self.line_sdt.text()
        malop = self.line_malop.text()
        try:
            self.cur.execute(
                "INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, DiaChi, Email, SoDienThoai, MaLop) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (masv, hoten, ngaysinh, gioitinh, diachi, email, sdt, malop))
            self.conn.commit()
            self.load_data()
            QtWidgets.QMessageBox.information(None, "Thành công", "Thêm sinh viên thành công")
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Sinh viên có ID này đã tồn tại")

    def update_student(self):
        masv = self.line_masv.text()
        hoten = self.line_name.text()
        ngaysinh = self.line_ngsinh.text()
        gioitinh = self.box_gioitinh.currentText()
        diachi = self.line_diachi.text()
        email = self.line_email.text()
        sdt = self.line_sdt.text()
        malop = self.line_malop.text()
        try:
            self.cur.execute(
                "UPDATE SinhVien SET HoTen=?, NgaySinh=?, GioiTinh=?, DiaChi=?, Email=?, SoDienThoai=?, MaLop=? WHERE MaSV=?",
                (hoten, ngaysinh, gioitinh, diachi, email, sdt, malop, masv))
            self.conn.commit()
            self.load_data()
            QtWidgets.QMessageBox.information(None, "Thành công", "Học viên cập nhật thành công")
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Sinh viên có ID này không tồn tại")

    def delete_student(self):
        masv = self.line_masv.text()
        try:
            self.cur.execute("DELETE FROM SinhVien WHERE MaSV=?", (masv,))
            self.conn.commit()
            self.load_data()
            QtWidgets.QMessageBox.information(None, "Thành công", "Xóa sinh viên thành công")
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(None, "Lỗi", "Sinh viên có ID này không tồn tại")

    def search_student(self):
        keyword = self.line_timkiem.text()
        query = f"SELECT * FROM SinhVien WHERE MaSV LIKE '%{keyword}%' OR HoTen LIKE '%{keyword}%'"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.table_danhsach.setRowCount(0)
        for row in rows:
            rowPosition = self.table_danhsach.rowCount()
            self.table_danhsach.insertRow(rowPosition)
            for column, data in enumerate(row):
                self.table_danhsach.setItem(rowPosition, column, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())