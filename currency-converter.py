import json
import sys
from urllib.request import urlopen

from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton, QComboBox,
    QVBoxLayout, QListWidget, QHBoxLayout, QGridLayout
)


class Course(QObject):
    CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__courses = None
        self.isoCodes = list(self.courses()["Valute"].keys())

    def courses(self):
        if self.__courses is None:
            with urlopen(self.CBR_URL) as r:
                self.__courses = json.loads(r.read())
        return self.__courses
    
    def getValue(self, isoCode):
        courses = self.courses()

        if isoCode in courses['Valute']:
            return courses['Valute'][isoCode]['Value']

        return None
    
    def getNominal(self, isoCode):
        courses = self.courses()

        if isoCode in courses['Valute']:
            return courses['Valute'][isoCode]['Nominal']

        return None

    def getValutes(self):
        return self.isoCodes
    




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__course = Course()

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultLabel = QLabel('Сумма в ', self)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.convertBtn.setCheckable(True)
        self.clearBtn = QPushButton('Очистить', self)

        self.currencyBtn = QComboBox(self)
        self.currencyBtn.setEditable(True)
        self.currencyBtn.addItems(self.__course.getValutes())

    def initSignals(self):
        self.convertBtn.clicked.connect(self.convertIntoRub)
        self.convertBtn.clicked.connect(self.convertIntoAnotherCurrency)
        self.clearBtn.clicked.connect(self.clear)
       
    def initLayouts(self):
        self.w = QWidget(self)

        self.mainLayout = QGridLayout(self.w)
        self.mainLayout.setSpacing(10)

        self.mainLayout.addWidget(self.srcLabel, 1, 0)
        self.mainLayout.addWidget(self.srcAmount, 2, 0)
        self.mainLayout.addWidget(self.resultLabel, 3, 0)
        self.mainLayout.addWidget(self.currencyBtn, 3 , 1)
        self.mainLayout.addWidget(self.resultAmount, 4, 0)
        self.mainLayout.addWidget(self.convertBtn, 5, 0)
        self.mainLayout.addWidget(self.clearBtn, 6, 0)

        self.setCentralWidget(self.w)

    def convertIntoRub(self):
        value = self.srcAmount.value()
        currencyValue = self.__course.getValue(self.currencyBtn.currentText()) / self.__course.getNominal(self.currencyBtn.currentText())

        if value:
            self.resultAmount.setValue(value / currencyValue)

    def convertIntoAnotherCurrency(self):
        value = self.resultAmount.value()
        currencyValue = self.__course.getValue(self.currencyBtn.currentText()) / self.__course.getNominal(self.currencyBtn.currentText())

        if value:
            self.srcAmount.setValue(value * currencyValue)

    def clear(self):
        value_1 = self.srcAmount.value()
        value_2 = self.resultAmount.value()

        if value_1 or value_2:
            self.resultAmount.setValue(0)
            self.srcAmount.setValue(0)

    def convertBtnStatus(self):
        value_1 = self.srcAmount.value()
        value_2 = self.resultAmount.value()

        if (value_1 and value_2) or not (value_1 and value_2):
            self.convertBtn.setEnabled(False)
            #return False
        else:
            self.convertBtn.setEnabled(True)
            #return True

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F5:
            self.close()

        if e.key() == Qt.Key_Return:
            self.convertIntoRub()
            self.convertIntoAnotherCurrency()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())