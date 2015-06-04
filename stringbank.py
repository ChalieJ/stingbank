# coding: utf-8

import os
import sys
import base64
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot    # for connect pyqt slot

data = {}

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('String Bank')
        self.setGeometry(100,100,250,100)

        # 1st layout [ label | button | button ] ==========
        # add widget
        labGetString   = QtWidgets.QLabel('Get String')
        self.bt_copy   = QtWidgets.QPushButton('copy', self)
        self.bt_delete = QtWidgets.QPushButton('delete', self)

        # add button event
        self.bt_copy.clicked.connect(self.slot_copy_clipboard)
        self.bt_delete.clicked.connect(self.slot_delete_clipboard)

        # make layout & set widget
        hboxDescriptionList = QtWidgets.QHBoxLayout()
        hboxDescriptionList.addWidget(labGetString)
        hboxDescriptionList.addWidget(self.bt_copy)
        hboxDescriptionList.addWidget(self.bt_delete)

        # 2nd layout [ combobox ] ==========
        self.cbList = QtWidgets.QComboBox(self)
        self.cbList.activated.connect(self.slot_set_label)
        hboxList = QtWidgets.QHBoxLayout()
        hboxList.addWidget(self.cbList)

        # 3rd layout [ label ] - show save string
        labSetString = QtWidgets.QLabel('Set String')
        hboxDescriptionSave= QtWidgets.QHBoxLayout()
        hboxDescriptionSave.addWidget(labSetString)

        # layout [ empty space ]
        labTemp = QtWidgets.QLabel(' ')
        hboxTemp = QtWidgets.QHBoxLayout()
        hboxTemp.addWidget(labTemp)

        # 4th layout [ label ]
        self.labString = QtWidgets.QLabel()
        hboxString = QtWidgets.QHBoxLayout()
        hboxString.addWidget(self.labString)

        # 5th layout
        self.le = QtWidgets.QLineEdit(self)
        self.bt_save = QtWidgets.QPushButton('save', self)
        self.bt_save.clicked.connect(self.slot_save_clipboard)
        hboxSave = QtWidgets.QHBoxLayout()
        hboxSave.addWidget(self.le)
        hboxSave.addWidget(self.bt_save)

        # set textedit
        self.te = QtWidgets.QTextEdit(self)

        # add hboxlay out to a vertical layout 
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hboxDescriptionList)
        vbox.addLayout(hboxList)
        vbox.addLayout(hboxString)
        vbox.addLayout(hboxTemp)
        vbox.addLayout(hboxDescriptionSave)
        vbox.addLayout(hboxSave)
        vbox.addWidget(self.te)

        # set layout
        self.setLayout(vbox)

        self.data_load()

        # set clipboard...
        self.qclip = QtWidgets.QApplication.clipboard()

    # copy button event
    @pyqtSlot()
    def slot_copy_clipboard(self):
        self.qclip.setText(data[self.cbList.currentText()])

    # save button event
    @pyqtSlot()
    def slot_save_clipboard(self):
        # add item(combobox) & data structure
        self.cbList.addItem(self.le.text())
        data[self.le.text()] = self.te.toPlainText()
        # refresh item
        self.refresh_item()

        # save file
        self.data_save()	

        self.te.clear()
        self.le.clear()

    # delete button event
    @pyqtSlot()
    def slot_delete_clipboard(self):
        if len(data):
            # delete structure
            del data[self.cbList.currentText()]

            # delete combobox item - current item
            self.cbList.removeItem(self.cbList.findText(self.cbList.currentText()))

            # refresh item
            self.refresh_item()
	
        # save file
        self.data_save()	

    # combobox event
    @pyqtSlot()
    def slot_set_label(self):
        self.labString.setText(data[self.cbList.currentText()])

    def data_save(self):
        fd = open("data.dat", "w")

        for (key, value) in data.items():
            fd.write(key + '|' + value + '\n')

        fd.close()
        self.sort_refresh_item()

    def data_load(self):
        if os.path.exists("data.dat"):
            fd = open("data.dat", "r")

            line = fd.readline()

            if len(line) == 0:
                return

            if line[-1] == "\n":
                line = line[:-1]

            while line:
                if len(line) > 0:
                    if line[-1] == "\n":
                        line = line[:-1]
                    splittext = line.split('|')
                    data[splittext[0]] = splittext[1]
                    self.cbList.addItem(splittext[0])
                    self.labString.setText(splittext[1])
                    line = fd.readline()

            self.sort_refresh_item()

            fd.close()
            self.refresh_item()	

    def refresh_item(self):
        if len(data):
            self.labString.setText(data[self.cbList.currentText()])
        else:
            self.labString.clear()

    def sort_refresh_item(self):
        sortKey = sorted(data)

        self.cbList.clear()

        for key in sortKey:
            self.cbList.addItem(key)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

