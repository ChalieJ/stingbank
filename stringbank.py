# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함

data = {}

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('String Bank')
        self.setGeometry(100,100,250,100)

        labGetString = QtWidgets.QLabel('Get String')
        self.bt_copy = QtWidgets.QPushButton('copy', self)
        self.bt_delete = QtWidgets.QPushButton('delete', self)
        self.bt_copy.clicked.connect(self.slot_copy_clipboard_1)
        hboxDescriptionList = QtWidgets.QHBoxLayout()
        hboxDescriptionList.addWidget(labGetString)
        hboxDescriptionList.addWidget(self.bt_copy)
        hboxDescriptionList.addWidget(self.bt_delete)

        labSetString = QtWidgets.QLabel('Set String')
        hboxDescriptionSave= QtWidgets.QHBoxLayout()
        hboxDescriptionSave.addWidget(labSetString)

        self.cbList = QtWidgets.QComboBox(self)
        self.cbList.activated.connect(self.slot_set_label)
        hboxList = QtWidgets.QHBoxLayout()
        hboxList.addWidget(self.cbList)

        self.labString = QtWidgets.QLabel()
        hboxString = QtWidgets.QHBoxLayout()
        hboxString.addWidget(self.labString)

        self.le = QtWidgets.QLineEdit(self)
        self.bt_save = QtWidgets.QPushButton('save', self)
        self.bt_save.clicked.connect(self.slot_save_clipboard_2)
        hboxSave = QtWidgets.QHBoxLayout()
        hboxSave.addWidget(self.le)
        hboxSave.addWidget(self.bt_save)

        labTemp = QtWidgets.QLabel('  ')
        hboxTemp = QtWidgets.QHBoxLayout()
        hboxTemp.addWidget(labTemp)

        self.te = QtWidgets.QTextEdit(self)
 
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hboxDescriptionList)
        vbox.addLayout(hboxList)
        vbox.addLayout(hboxString)
        vbox.addLayout(hboxTemp)
        vbox.addLayout(hboxDescriptionSave)
        vbox.addLayout(hboxSave)
        vbox.addWidget(self.te)
 
        self.setLayout(vbox)
 
        self.qclip = QtWidgets.QApplication.clipboard()
 
    @pyqtSlot()
    def slot_copy_clipboard_1(self):
        self.qclip.setText(data[self.cbList.currentText()])
 
    @pyqtSlot()
    def slot_save_clipboard_2(self):
        self.cbList.addItem(self.le.text())
        data[self.le.text()] = self.te.toPlainText()
        self.labString.setText(data[self.cbList.currentText()])

    @pyqtSlot()
    def slot_set_label(self):
        self.labString.setText(data[self.cbList.currentText()])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

