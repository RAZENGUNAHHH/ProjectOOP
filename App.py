import sys
from PyQt6.QtCore import QSize, Qt, QRectF
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QFont, QPalette 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox , QDialog ,QLabel ,QVBoxLayout ,QLineEdit
from Cinema_system import *
class CinemaBookingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Booking Cinema")
        self.showFullScreen()
        self.__image_seat_regular = QPixmap("seat.png").scaled(50, 50)  # load รูปภาพ regular
        self.__image_seat_vip = QPixmap("vip.png").scaled(50, 50)  # load รูปภาพ vip
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
        self.setPalette(palette)
        self.__cinema = CinemaHall(50) # set ค่าที่นั่ง 
        self.__main_layout = QGridLayout()  # สร้าง QGridLayout สำหรับจัดวางปุ่ม
        self.__main_layout.setContentsMargins(300,300,300,300)
        self.setLayout(self.__main_layout)
        self.display_seat(self.__main_layout)
        
        # สร้างปุ่มปิดโปรแกรม
        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close_app)
        self.__main_layout.addWidget(self.close_button, 11, 0, 1, 10)  # เพิ่มปุ่มลงใน main_layout

    def close_app(self):
        self.close()

    # แสดงเก้าอี้ทั้งหมด เริ่มต้น  ทั้ง vip และ regular 
    def display_seat(self , main_layout):
        # สร้างปุ่ม Regular
        for row in range(5):
            for col in range(10):
                seat_number = row * 10 + col
                if seat_number < 30:
                        s_VIP = VIPSeat(seat_number,500)
                        self.__cinema.add_seat(s_VIP , seat_number)
                        self.draw_seat(seat_number, main_layout, row, col)
                else:
                        s_Re = RegularSeat(seat_number,200)
                        self.__cinema.add_seat(s_Re , seat_number)
                        self.draw_seat_vip(seat_number, main_layout, row, col)

    
    # update seat
    def display_update(self):
        for row in range(5):
            for col in range(10):
                seat_number = row * 10 + col
                if seat_number < 30:
                        isBooked = self.__cinema.get_number_seat(seat_number).get_booked()
                        if not isBooked:
                           self.draw_seat(seat_number, self.__main_layout, row, col)
                else:
                        isBooked = self.__cinema.get_number_seat(seat_number).get_booked()
                        if not isBooked:
                           self.draw_seat_vip(seat_number, self.__main_layout, row, col)
             

    # วาดหน้าจอโรงหนัง
    def paintEvent(self,event):
        screen = QRectF(1300 / 2, 30, 600, 100)
        margin = 0
        movie_title = QRectF(screen.x() + margin, screen.y() + margin, screen.width() - 2 * margin, screen.height() - 2 * margin)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.GlobalColor.black)
        painter.setFont(QFont("Arial", 20))
        painter.drawText(movie_title, Qt.AlignmentFlag.AlignHCenter, "Conjuring")
        painter.drawRect(screen)

    # วาดเก้าอี้ regular
    def draw_seat(self, number, layout, row, col):
        icon_button = QPushButton(QIcon(self.__image_seat_regular), '', self)
        icon_button.setStyleSheet('border: none;')
        icon_button.setIconSize(QSize(50, 50))
        layout.addWidget(icon_button, row, col)
        icon_button.clicked.connect(lambda: self.booking_seat(number))
  # วาดเก้าอี้ vip
    def draw_seat_vip(self, number, layout, row, col):
        icon_button = QPushButton(QIcon(self.__image_seat_vip), '', self)
        icon_button.setStyleSheet('border: none;')
        icon_button.setIconSize(QSize(50, 50))
        layout.addWidget(icon_button, row + 3, col)
        icon_button.clicked.connect(lambda: self.booking_seat(number))

    # ui เมือกดคลิกที่ปุ่ม
    def booking_seat(self, number):
        if number >= 30:
             self.ui_booking('VIP' , number , 500)
        else:
            self.ui_booking('Regular', number , 200)

    # ui เมือกดคลิกที่ปุ่ม เพื่อรับค่าการจอง
    def ui_booking(self,seat_type , number , price):
        message = f'{seat_type} Seat'

        dialog = QDialog(self)
        dialog.setWindowTitle(message)

        layout = QVBoxLayout()

        name_label = QLabel("Name:")
        layout.addWidget(name_label)
        name_input = QLineEdit()
        layout.addWidget(name_input)

        price_label = QLabel("Price:")
        layout.addWidget(price_label)
        price_input = QLineEdit()
        price_input.setText(f'{price}')  # กำหนดค่า default เป็น "100"
        price_input.setReadOnly(True)  # ตั้งค่าเป็นค่าคงที่
        layout.addWidget(price_input)

        seat_label = QLabel("Seat_Number:")
        layout.addWidget(seat_label)
        seat_input = QLineEdit()
        seat_input.setText(f'{number}')  # กำหนดค่า default เป็น "100"
        seat_input.setReadOnly(True)  # ตั้งค่าเป็นค่าคงที่
        layout.addWidget(seat_input)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_booking(dialog, number , name_input.text()))
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec()

    # เมื่อกดจอง
    def on_ok_booking(self, dialog, number, name):
        if not name:
            self.display_messagebox('Please enter your name.')
            return
        this_seat = self.__cinema.get_number_seat(number)
        this_seat.book()
        this_seat.set_name(name)
        # ลบทุกปุ่มที่อยู่บน main_layout
        for i in reversed(range(self.__main_layout.count())):
            widget = self.__main_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        # วาดปุ่มใหม่ตามสถานะปัจจุบันของที่นั่ง
        self.display_update()
        dialog.accept()

    # เอาไว้ สร้าง messagebox
    def display_messagebox(self  , message):
        # สร้าง QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Search result")
        msg_box.setText(message)
        msg_box.setInformativeText("Please try again")
        msg_box.setIcon(QMessageBox.Icon.Warning)  # เพิ่มไอคอนเตือน
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        # แสดง Message Box และรอผลลัพธ์
        msg_box.exec()

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CinemaBookingApp()
    sys.exit(app.exec())