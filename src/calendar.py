from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Calendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
    def paintCell(self, paint, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, paint, rect, date)
        if date == date.currentDate():
            paint.setBrush(QtGui.QColor(0, 200, 200, 50))
            paint.drawRect(rect)
        if date > date.currentDate():
            paint.setBrush(QtGui.QColor(0, 200, 0, 0))
            paint.drawRect(rect)