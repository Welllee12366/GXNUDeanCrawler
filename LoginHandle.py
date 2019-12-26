# !/bin/bash
# -*- coding:utf-8 -*-

from Crawler import DeanCrawler
from Ui_login import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from PyQt5.QtGui import QPixmap

class LoginHandle:

    def __init__(self,ui):
        self.crawler = DeanCrawler()
        self.crawler.init_cookiejar()
        self.ui = ui

    def setCaptchaImage(self):
        self.ui.img_cap.setPixmap(QPixmap(self.getCaptcha()))

    def getCaptcha(self):
        return self.crawler.CrawleCaptcha()

    def init_logo(self):
        self.ui.logo_label.setPixmap(QPixmap('./logo.jpg'))
        self.ui.logo_label.setScaledContents(True)

    def doLogin(self):
        username = self.ui.username.text()
        password  = self.ui.password.text()
        captcha = self.ui.captcha.text()
        if(username == '' or password == '' or captcha == ''):
            return '用户名/密码或验证码不能为空'
        self.crawler.setLoginInfo(username, password, captcha)
        if not self.crawler.Login():
            return '用户名/密码或验证码错误'
        return True

    def printScores(self):
        print(self.crawler.TotalScore())

    def printInternalExams(self):
        print(self.crawler.InternalExamScores())


