# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함

data = {}

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100,100,250,100)
 
        self.cb = QtWidgets.QComboBox(self)
        self.cb.activated.connect(self.slot_set_label)
        self.bt_1 = QtWidgets.QPushButton('copy', self)
        self.bt_1.clicked.connect(self.slot_copy_clipboard_1)
        hbox_1 = QtWidgets.QHBoxLayout()
        hbox_1.addWidget(self.cb)
        hbox_1.addWidget(self.bt_1)

        self.labString = QtWidgets.QLabel()
        hbox_2 = QtWidgets.QHBoxLayout()
        hbox_2.addWidget(self.labString)

        self.le = QtWidgets.QLineEdit(self)
        self.bt_2 = QtWidgets.QPushButton('save', self)
        self.bt_2.clicked.connect(self.slot_save_clipboard_2)
        hbox_3 = QtWidgets.QHBoxLayout()
        hbox_3.addWidget(self.le)
        hbox_3.addWidget(self.bt_2)
 
        self.te = QtWidgets.QTextEdit(self)
 
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addWidget(self.te)
 
        self.setLayout(vbox)
 
        self.qclip = QtWidgets.QApplication.clipboard()
 
    @pyqtSlot()
    def slot_copy_clipboard_1(self):
        self.qclip.setText(data[self.cb.currentText()])
 
    @pyqtSlot()
    def slot_save_clipboard_2(self):
        self.cb.addItem(self.le.text())
        data[self.le.text()] = self.te.toPlainText()
        self.labString.setText(data[self.cb.currentText()])

    @pyqtSlot()
    def slot_set_label(self):
        self.labString.setText(data[self.cb.currentText()])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

