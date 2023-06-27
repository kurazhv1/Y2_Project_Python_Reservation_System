import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication, QDesktopWidget, QWidget,
                             QLabel, QVBoxLayout, QLineEdit,
                             QTextEdit, QGridLayout, QMessageBox, QComboBox, QHBoxLayout, QGroupBox, QToolButton)
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import check_reservation
from calendar import Calendar

class MainMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initial_UI()

    def initial_UI(self):
        # buttons:
        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(QApplication.instance().quit)
        exit_button.resize(exit_button.sizeHint())
        exit_button.move(50, 50)

        reservation_button = QPushButton('New Reservation', self)
        reservation_button.clicked.connect(self.reservation_window)

        self.resize(200, 500)
        menu = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        menu.moveCenter(center_point)
        self.move(menu.topLeft())

        self.setWindowTitle('Main Menu')
        self.show()

    def reservation_window(self):
        self.w = ReservationWindow()
        self.close()


class ReservationWindow(QWidget):
    date_form = 'dd.MM.yyyy'
    def __init__(self):
        super().__init__()
        self.reservationUI()

    def reservationUI(self):

        name = QLabel('Name')
        phone = QLabel('Phone number')
        room_number = QLabel('Room number (1...8)')
        self.room_number_box = QComboBox(self)
        self.room_number_box.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])
        button_reserve = QPushButton("Reserve", self)
        button_back = QPushButton("Back", self)
        self.nameLE = QLineEdit(self)
        self.phoneLE = QLineEdit(self)

        self.calendar_Start = Calendar()
        self.calendar_End = Calendar()
        start_date = QLabel('Start date')
        end_date = QLabel('End date')
        self.start_dateLE =  QtWidgets.QLineEdit(placeholderText="DD.MM.YYYY")
        self.end_dateLE =  QtWidgets.QLineEdit(placeholderText="DD.MM.YYYY")

        # Button for Start date
        self.button_Start = QtWidgets.QToolButton()
        self.button_Start.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))
        self.calendar_Start.setWindowFlags(QtCore.Qt.Popup)
        self.calendar_Start.installEventFilter(self)

        #Button for End date
        self.button_End = QtWidgets.QToolButton()
        self.button_End.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))

        self.calendar_End.setWindowFlags(QtCore.Qt.Popup)
        self.calendar_End.installEventFilter(self)



        #layout

        self.calendar_window = QWidget()
        calendar_box = QGridLayout()
        # adding widgets
        calendar_box.addWidget(name, 1, 0)
        calendar_box.addWidget(self.nameLE, 1, 1)

        calendar_box.addWidget(phone, 2, 0)
        calendar_box.addWidget(self.phoneLE, 2, 1)

        calendar_box.addWidget(room_number, 3, 0)
        calendar_box.addWidget(self.room_number_box, 3, 1)
        calendar_box.addWidget(start_date, 4, 0)
        calendar_box.addWidget(end_date, 5, 0)
        calendar_box.addWidget(self.start_dateLE, 4, 1)
        calendar_box.addWidget(self.end_dateLE, 5, 1)

        calendar_box.addWidget(button_reserve,6,2)
        calendar_box.addWidget(button_back, 6, 0)

        calendar_box.addWidget(self.button_Start, 4, 2)
        calendar_box.addWidget(self.button_End, 5, 2)


        self.calendar_window.setLayout(calendar_box)





        self.calendar_window.setGeometry(300, 300, 415, 350)
        self.calendar_window.setWindowTitle('Reservation')
        self.calendar_window.show()


    #Implement date selections if needed
        selected_date = self.calendar_End.selectedDate()
        selected_day = self.calendar_End.selectedDate().day()
        selected_month = self.calendar_End.selectedDate().month()
        selected_year = self.calendar_End.selectedDate().year()
    #Implement next button to make reservation
        #connections
        self.button_Start.pressed.connect(self.popupStartCal)
        self.button_Start.released.connect(self.calendar_Start.hide)

        self.calendar_Start.clicked.connect(self.set_Start_Date)
        self.calendar_Start.activated.connect(self.set_Start_Date)

        self.button_End.pressed.connect(self.popupEndCal)
        self.button_End.released.connect(self.calendar_End.hide)

        self.calendar_End.clicked.connect(self.set_End_Date)
        self.calendar_End.activated.connect(self.set_End_Date)

        button_reserve.clicked.connect(self.make_reserve)
        button_back.clicked.connect(self.back_button)




    def back_button(self):
        self.mm = MainMenu()
        self.mm.show()
        self.calendar_window.close()


    def popupStartCal(self):
        mpk = self.start_dateLE.mapToGlobal(self.end_dateLE.rect().bottomLeft())
        mpk += QtCore.QPoint(0, 1)
        geom = QtCore.QRect(mpk, self.calendar_Start.sizeHint())
        self.calendar_Start.setGeometry(geom)
        self.calendar_Start.show()
        self.calendar_Start.setFocus()
    def popupEndCal(self):
        mpk = self.end_dateLE.mapToGlobal(self.end_dateLE.rect().bottomLeft())
        mpk += QtCore.QPoint(0, 1)
        rect = QtCore.QRect(mpk, self.calendar_End.sizeHint())
        self.calendar_End.setGeometry(rect)
        self.calendar_End.show()
        self.calendar_End.setFocus()



    def set_Start_Date(self, date):
        self.start_dateLE.setText(date.toString(self.date_format()))
        self.calendar_Start.setSelectedDate(date)
        self.calendar_Start.hide()
    def set_End_Date(self, date):
        self.end_dateLE.setText(date.toString(self.date_format()))
        self.calendar_End.setSelectedDate(date)
        self.calendar_End.hide()




    def date_format(self):
        return self.date_form or QtCore.QLocale().dateFormat(QtCore.QLocale.ShortFormat)

    def make_reserve(self):

        client_name = self.nameLE.text()
        phone = self.phoneLE.text()
        room = str(self.room_number_box.currentText())
        start = str(self.start_dateLE.text())
        end = str(self.end_dateLE.text())
        if check_reservation.make_reserv(start, end, room):
            print("Great job")
        else:
            print("smthng wrong:С")



def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
