# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, addr):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 122)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 421, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, addr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, addr):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your private key"))
        self.lineEdit.setText(_translate("MainWindow", "i just shit at my ass"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy"))
        self.lineEdit.setText(self.findhash(addr))
        self.pushButton_2.clicked.connect(self.copia(addr))

    def findhash(self, addr):
        with open('data/addresslist.txt', 'r') as f:
            lines=f.readlines()
        global hash
        for l in lines:
            if l[:16]==addr:
                hash=l[17:]
        hash=hash.strip('\n')
        return(hash)

    def copia(self, addr):
        cmd='echo '+addr+':'+hash+' | clip'
        print(hash)
        subprocess.check_call(cmd, shell=True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
