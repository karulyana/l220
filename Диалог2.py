import sys
import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.Qt import pyqtSignal


class Dialog2(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 600)                        # Размеры окна.
        self.move(1380,225)
        self.setWindowTitle('Выход')              # Нидпись в заголовке.
        # self.setWindowIcon(QIcon('./Icon/edit1'))  # Иконка прложения.
        self.grid()

    def grid(self):
        self.gride = QGridLayout()
        self.table = TableWidget()
        self.gride.addWidget(self.table)
        self.setLayout(self.gride)

    def close(self):
        self.close()

class TableWidget(QTableWidget):
    my_signal = pyqtSignal(list)

    def __init__(self, parent=None, data=[]):
        super(TableWidget, self).__init__(parent)
        self.update()
        self.my_signal.connect(self.update)

    def my_slot_update(self, data):
        print(data, flush=True)
        self.update()

    def update(self, data=[]):
        self.setColumnCount(1)
        self.setRowCount(len(data))
        for i, entry in enumerate(data, start=1):
            self.setRowCount(i)
            item = QTableWidgetItem()
            item.setText(str(entry))
            self.setItem(i - 1, 0, item)
        #print(data)