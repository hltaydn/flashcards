# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(400, 400)
        loginwindow.setMinimumSize(QtCore.QSize(400, 400))
        loginwindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -20, 400, 400))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 102), stop:0.326316 rgba(255, 0, 0, 130), stop:0.339799 rgba(255, 255, 255, 255), stop:0.636842 rgba(255, 255, 255, 135), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 95));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 141, 40))
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.username_edit = QtWidgets.QLineEdit(self.groupBox)
        self.username_edit.setGeometry(QtCore.QRect(180, 180, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.username_edit.setFont(font)
        self.username_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_edit.setText("")
        self.username_edit.setObjectName("username_edit")
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        self.login_button.setGeometry(QtCore.QRect(90, 250, 228, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_button.setObjectName("login_button")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 155, 40))
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        loginwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        loginwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginwindow)
        self.statusbar.setObjectName("statusbar")
        loginwindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Login"))
        self.label_2.setText(_translate("loginwindow", "User name:"))
        self.login_button.setText(_translate("loginwindow", "Login"))
        self.label_3.setText(_translate("loginwindow", "PyBoys Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())