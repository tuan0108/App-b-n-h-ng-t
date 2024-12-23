from PyQt6 import QtCore, QtGui, QtWidgets
import webbrowser
import subprocess


class Ui_MainWindow(object):
    def open_themmonhoc(self):
        subprocess.run(["python", "ThemMonHoc.py"])

    def open_themtk(self):
        subprocess.run(["python", "ThemTaiKhoan.py"])

    def open_gv(self):
        subprocess.run(["python", "infoGV.py"])

    def open_sv(self):
        subprocess.run(["python", "Sinhvienadmin.py"])

    def open_lop(self):
        subprocess.run(["python", "ThemLop.py"])

    def open_pc(self):
        subprocess.run(["python", 'phanconglich.py'])

    def open_baocao(self):
        subprocess.run(["python", 'baocao.py'])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/logo.jpg"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Stylesheet for buttons with border
        button_style = """
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                color: white;
                border: 2px solid #3498db;
                border-radius: 5px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #3498db;
                border-color: #2980b9;
            }
            QPushButton:checked {
                background-color: #2980b9;
                border-color: #2980b9;
            }
        """

        self.taikhoan = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.taikhoan.setStyleSheet(button_style)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.taikhoan.setIcon(icon)
        self.taikhoan.setIconSize(QtCore.QSize(14, 14))
        self.taikhoan.setCheckable(True)
        self.taikhoan.setAutoExclusive(True)
        self.taikhoan.setObjectName("taikhoan")
        self.verticalLayout_2.addWidget(self.taikhoan)

        # Repeat similar setup for other buttons
        self.giangvien = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.giangvien.setStyleSheet(button_style)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.giangvien.setIcon(icon1)
        self.giangvien.setIconSize(QtCore.QSize(14, 14))
        self.giangvien.setCheckable(True)
        self.giangvien.setAutoExclusive(True)
        self.giangvien.setObjectName("giangvien")
        self.verticalLayout_2.addWidget(self.giangvien)

        self.sinhvien = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.sinhvien.setStyleSheet(button_style)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-48.ico"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.sinhvien.setIcon(icon2)
        self.sinhvien.setIconSize(QtCore.QSize(14, 14))
        self.sinhvien.setCheckable(True)
        self.sinhvien.setAutoExclusive(True)
        self.sinhvien.setObjectName("sinhvien")
        self.verticalLayout_2.addWidget(self.sinhvien)

        self.lop = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.lop.setStyleSheet(button_style)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.lop.setIcon(icon3)
        self.lop.setIconSize(QtCore.QSize(14, 14))
        self.lop.setCheckable(True)
        self.lop.setAutoExclusive(True)
        self.lop.setObjectName("lop")
        self.verticalLayout_2.addWidget(self.lop)

        self.phancong = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.phancong.setStyleSheet(button_style)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.phancong.setIcon(icon4)
        self.phancong.setIconSize(QtCore.QSize(14, 14))
        self.phancong.setCheckable(True)
        self.phancong.setAutoExclusive(True)
        self.phancong.setObjectName("phancong")
        self.verticalLayout_2.addWidget(self.phancong)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.hocphan = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.hocphan.setStyleSheet(button_style)
        self.hocphan.setObjectName("hocphan")
        self.verticalLayout_4.addWidget(self.hocphan)

        self.baocao = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.baocao.setStyleSheet(button_style)
        self.baocao.setObjectName("baocao")
        self.verticalLayout_4.addWidget(self.baocao)

        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        self.exit_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        self.exit_btn_2.setStyleSheet(button_style)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icon/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)

        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        # Add "Previous" and "Next" buttons to switch images
        self.prev_btn = QtWidgets.QPushButton(self.widget)
        self.prev_btn.setText("<-")
        self.prev_btn.setObjectName("prev_btn")
        self.horizontalLayout.addWidget(self.prev_btn)

        self.next_btn = QtWidgets.QPushButton(self.widget)
        self.next_btn.setText("->")
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)

        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")

        # Initialize stacked widget to empty
        self.stackedWidget.setCurrentIndex(-1)

        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn_2.clicked.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize image paths and URLs
        self.image_data = [
            {"path": "spg1.jpg", "url": "https://career.gpo.vn/tim-hieu-ve-nganh-he-thong-thong-tin-quan-ly-a1227.html"},
            {"path": "spg2.jpg", "url": "https://inbusinessnews.reporter.com.cy/article/2024/2/27/761111/etoimes-gia-metaskhematismo-oi-etaireies-oi-proteraiotetes-ton-ceos-kai-oi-prooptikes-gia-to-2024/"},
            {"path": "spg3.jpg", "url": "https://swinburne-vn.edu.vn/review-nganh-he-thong-thong-tin-quan-ly/"}
        ]

        # Add image labels to stacked widget and connect click events
        for data in self.image_data:
            label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(data["path"])
            label.setPixmap(pixmap)
            label.setScaledContents(True)  # Adjust image size automatically
            label.mousePressEvent = lambda event, url=data["url"]: self.open_url(url)  # Connect click event
            self.stackedWidget.addWidget(label)

        # Initialize timer to switch images
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(3000)

        # Connect button click events to image switch methods
        self.prev_btn.clicked.connect(self.prev_image)
        self.next_btn.clicked.connect(self.next_image)

        self.taikhoan.clicked.connect(self.open_themtk)
        self.giangvien.clicked.connect(self.open_gv)
        self.sinhvien.clicked.connect(self.open_sv)
        self.lop.clicked.connect(self.open_lop)
        self.phancong.clicked.connect(self.open_pc)
        self.hocphan.clicked.connect(self.open_themmonhoc)
        self.baocao.clicked.connect(self.open_baocao)
        self.exit_btn_2.clicked.connect(exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "MENU"))
        self.taikhoan.setText(_translate("MainWindow", "Tài khoản"))
        self.giangvien.setText(_translate("MainWindow", "Giảng viên"))
        self.sinhvien.setText(_translate("MainWindow", "Sinh viên"))
        self.lop.setText(_translate("MainWindow", "Lớp"))
        self.phancong.setText(_translate("MainWindow", "Phân công"))
        self.hocphan.setText(_translate("MainWindow", "Học phần"))
        self.baocao.setText(_translate("MainWindow", "Thống kê và báo cáo"))
        self.exit_btn_2.setText(_translate("MainWindow", "Đăng xuất"))

    def next_image(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)

    def prev_image(self):
        current_index = self.stackedWidget.currentIndex()
        prev_index = (current_index - 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(prev_index)

    def open_url(self, url):
        webbrowser.open(url)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
