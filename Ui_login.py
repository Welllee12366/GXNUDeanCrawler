# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Well\PycharmProjects\DeanGUI\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import LoginHandle

from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.handle = LoginHandle.LoginHandle(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 239)
        MainWindow.setFixedSize(359, 239)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.log_btn = QtWidgets.QPushButton(self.centralWidget)
        self.log_btn.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.log_btn.setObjectName("log_btn")
        self.can_btn = QtWidgets.QPushButton(self.centralWidget)
        self.can_btn.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.can_btn.setObjectName("can_btn")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(240, 210, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 54, 12))
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.centralWidget)
        self.username.setGeometry(QtCore.QRect(190, 40, 121, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralWidget)
        self.password.setGeometry(QtCore.QRect(190, 70, 121, 20))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.captcha = QtWidgets.QLineEdit(self.centralWidget)
        self.captcha.setGeometry(QtCore.QRect(190, 100, 121, 20))
        self.captcha.setObjectName("captcha")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 41, 16))
        self.label_4.setObjectName("label_4")
        self.logo_label = QtWidgets.QLabel(self.centralWidget)
        self.logo_label.setGeometry(QtCore.QRect(20, 30, 101, 91))
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.img_cap = QtWidgets.QLabel(self.centralWidget)
        self.img_cap.setGeometry(QtCore.QRect(190, 130, 121, 41))
        self.img_cap.setObjectName("img_cap")
        self.cap_btn = QtWidgets.QPushButton(self.centralWidget)
        self.cap_btn.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.cap_btn.setObjectName("cap_btn")
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        self.ConectDefine()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "广西师范大学教务处认证页面"))

        self.log_btn.setText(_translate("MainWindow", "登录"))
        self.can_btn.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "Powered By WellLee"))
        self.label_2.setText(_translate("MainWindow", "账号"))
        self.label_3.setText(_translate("MainWindow", "密码"))
        self.label_4.setText(_translate("MainWindow", "验证码"))
        self.img_cap.setText(_translate("MainWindow", "      Captcha"))
        self.cap_btn.setText(_translate("MainWindow", "获取验证码"))
        self.handle.init_logo()
        self.handle.setCaptchaImage()

    def ConectDefine(self):
        self.cap_btn.clicked.connect(self.generateCaptcha)
        self.log_btn.clicked.connect(self.login)
        self.can_btn.clicked.connect(self.cancel)

    def generateCaptcha(self):
        self.handle.setCaptchaImage()

    def login(self):
        result = self.handle.doLogin()
        if str == type(result):
            msg_box = QMessageBox
            msg_box.warning(self, '警告', result, msg_box.Cancel)
            self.generateCaptcha()
        else:
            QMessageBox.warning(self, 'Success', '登录成功', QMessageBox.Ok)
        pass

    def cancel(self):
        self.username.setText('')
        self.password.setText('')
        self.captcha.setText('')
        self.handle.printInternalExams()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

