﻿# -*- coding:utf-8 -*-
import re
from urllib.request import Request
import urllib.request
import urllib.parse
from http.cookiejar import CookieJar
from Config import Config
from bs4 import BeautifulSoup
import time
from pathlib import Path
import os
"""
    类名：DeanCrawler
    作用：封装教务处爬虫相关类，提供一些基本接口
    参数：用户名，密码
    Author：WellLee
    最后一次修改时间：2018年1月15日 11:44:33
"""
class DeanCrawler:
    """
        方法名：__init__
        作用：初始化参数
        参数：用户名，密码
        返回值：NULL
        最后一次修改时间：2018年1月14日 18:52:29
    """
    def __init__(self, username='', password=''):
        self.__browser = None
        self.__config = Config()
        self.__username = username
        self.__password = password
        self.__curPage = None
        #self.Login()
    """
        方法名：init_cookiejar
        作用：初始化Cookie环境
        参数: self
        返回值: None
        最后一次修改时间: 2019年12月26日 11:25:31
    """
    def init_cookiejar(self):
        loginURL = self.__config.get('loginEntryURL')
        cookiejar = CookieJar()
        self.__browser = urllib.request.HTTPCookieProcessor(cookiejar)
        self.__browser = urllib.request.build_opener(self.__browser)
        request = Request(loginURL)
        response = self.__browser.open(request)
        self.__curPage = response.read().decode('utf-8')
        pass
    """
        方法名：CrawleCaptcha
        作用：抓取验证码
        参数: self
        返回值: 验证码存储路径
        最后一次修改时间: 2019年12月26日 11:25:31
    """
    def CrawleCaptcha(self):
        img = self.__browser.open("http://172.16.130.20/dean/student/captcha/dean")
        img = img.read()
        dirpath = Path('./path')
        if dirpath.exists() :
            imgpath = './path/' + str(int(time.time())) + '.png'
        else:
            os.mkdir('./path')
            imgpath = './path/' + str(int(time.time())) + '.png'
        with open(imgpath, 'wb') as f:
            f.write(img)
        return imgpath
    """
        方法名：setLoginInfo
        作用：设置用户密码参数
        参数：self
        返回值：True/False
        最后一次修改时间：2018年1月14日 18:52:29
    """
    def setLoginInfo(self, username, password, captcha):
        self.__username = username
        self.__password = password
        self.__captcha = captcha
        pass

    """
        方法名：Login
        作用：完成教务处认证
        参数：self
        返回值：True/False
        最后一次修改时间：2018年1月14日 18:52:29
    """
    def Login(self):
        obj = '<input type="hidden" name="_token" value="(.+)">'  # Regular Expression pattern
        pattern = re.compile(obj)
        xsrf = pattern.findall(self.__curPage)[0]  # Get the xsrf use the Regular Expression
        logindata = {
            "_token": xsrf,
            "username": self.__username,
            "password": self.__password,
            "captcha":  self.__captcha
        }
        postdata = urllib.parse.urlencode(logindata).encode('utf-8')
        loginURL = self.__config.get('loginEntryURL')
        request = Request(loginURL, postdata)
        response = self.__browser.open(request)
        try:
            self.__curPage = response.read().decode('utf-8')
        except:
            return False
        obj = '<h3 class="panel-title">学生登录</h3>'
        pattern = re.compile(obj)
        result = pattern.findall(self.__curPage)
        if len(result) != 0:
            return False
        return True
    """
        方法名：getcurrentPage
        作用：获取当前访问的页面
        参数：self
        返回值：当前保存的页面（str）
        最后一次修改时间：2018年1月15日 11:44:23
    """
    def getcurrentPage(self):
        return self.__curPage

    """
        方法名：classtabel
        作用：爬取选课课程表数据
        参数：self
        返回值：选课课程数据（List）
        最后一次修改时间：2018年1月15日 11:44:20
    """
    def classtable(self):
        classtableURL = self.__config.get('selcourseURL')
        self.__curPage = self.__browser.open(classtableURL).read()
        soup = BeautifulSoup(self.__curPage, "html.parser")
        tbody = soup.select('html body div#wrapper main#page-wrapper article.row section.row div.col-sm-12 div.panel.panel-default div.panel-body div.table-responsive table.table.table-bordered.table-striped tbody tr td')
        cs_count = len(tbody)
        courses = {}
        temp = []
        for i in range(0, cs_count + 1):
            if(i % 11 == 0 and i != 0)  :
                courses[temp[1]] = temp
                temp = []
            if i < cs_count:
                temp.append(tbody[i].text)
        cs_final = []

        for course in courses:
            cs_list = []
            cs_list.append(courses[course][0])
            cs_list.append(course)
            for i in range(4, 11):
                if courses[course][i] != u'\n':
                    tempstr = courses[course][i]
                    tempstr = tempstr.split(u'\n')
                    cs_list.append('星期' + str(i-3))
                    cs_list.append(tempstr[2])
                    cs_list.append(tempstr[3])
                    cs_list.append(tempstr[4])
                    cs_list.append(tempstr[5])
            if len(cs_list) > 7 :
                cs_final.append(cs_list[:7])
                temp = []
                temp.append(cs_list[0])
                temp.append(cs_list[1])
                for i in cs_list[7:]:
                    temp.append(i)
                cs_final.append(temp)
            else:
                cs_final.append(cs_list)
        return cs_final
    """
        方法名：totalScore
        作用：爬取综合成绩单
        参数：self
        返回值：综合成绩单(List)
        最后一次修改时间：2018年1月15日 11:44:17
    """
    def TotalScore(self):
        scoresURL = self.__config.get('scores')
        self.__curPage = self.__browser.open(scoresURL).read()
        null = None
        try:
            jsondata = eval(self.__curPage)
        except:
            return []
        scores = jsondata['data']
        resultList = []
        for i in scores:
            id = i['pt'] + i['kcxz'] + i['kch']
            score = []
            score.append(id)
            score.append(i['cj'])
            score.append(i['course']['kcmc'])
            score.append(i['nd'])
            score.append(i['xq'])
            score.append(i['kh'])
            score.append(i['xf'])
            score.append(i['jd'])
            resultList.append(score)
        return resultList
    """
        方法名：InternalExamScores
        作用：爬取国家成绩表。
        参数：self
        返回值：国家成绩数据（list）
        最后一次修改时间：2018年1月15日 13:36:11
    """
    def InternalExamScores(self):
        examURL = self.__config.get('exam')
        self.__curPage = self.__browser.open(examURL).read()
        soup = BeautifulSoup(self.__curPage,  "html.parser")
        tbody = soup.select('html body div#wrapper main#page-wrapper article.row section.row div.col-sm-12 div.panel.panel-default div.panel-body div.table-responsive table.table.table-bordered.table-striped.table-hover tbody tr td')
        exam_count = len(tbody)
        exam_result = []
        temp = []
        for i in range(0, exam_count):
            if (i % 3 == 0 and i != 0):
                exam_result.append(temp)
                temp = []
            temp.append(tbody[i].text)
            if (i + 1) == exam_count:
                exam_result.append(temp)
        return exam_result
    """
        方法名：InternalExamScores
        作用：爬取待确认成绩数据
        参数：self
        返回值：待确认成绩(List)
        最后一次修改时间：2018年1月15日 13:36:17
    """
    def unconfirmedScore(self):
        unconfirmedURL = self.__config.get('UnconfirmedURL')
        self.__curPage = self.__browser.open(unconfirmedURL).read().decode('utf-8')
        obj = '<td.*>(.+)</td>'
        pattern = re.compile(obj)
        result = pattern.findall(self.__curPage)
        resultList = []
        temp = []
        for i in result:
            temp.append(i)
            if (i == u'作弊' or i == u'正常' or i == u'补考' or i == u'重修'):
                resultList.append(temp)
                temp = []
        return resultList
    """
        方法名：getName
        作用：获取用户的真实姓名
        参数：self
        返回值：姓名(List)
        最后一次修改时间：2018年2月19日 19:02:35
    """
    def getName(self):
        obj = '欢迎(.*)使用选课系统'
        pattern = re.compile(obj)
        result = pattern.findall(self.__curPage)
        return result

    """
        方法名：getcourseJSON
        作用：获取用户当前的课程JSON信息
        参数：self, url, campusID
        返回值：JSON数据
        最后一次修改时间：2018年6月26日 21:58:01
    """

    def getcourseJSON(self, url, campusID):
        urls = url + campusID
        print(urls)
        JSON = self.__browser.open(url + campusID).read()
        return JSON
    """
        方法名：e_dcourse
        作用：选课/退课
        参数：self, url, postdata
        返回值：服务器响应
        最后一次修改时间：2018年6月26日 21:58:01
    """
    def e_dcourse(self, url, postdata):
        postdata = urllib.parse.urlencode(postdata).encode('utf-8')
        request = Request(url, postdata)
        response = self.__browser.open(request)
        return response
    """
        方法名：generatePOSTDATA
        作用：根据用户退/选课需求动态生成POST数据
        参数：self, course, coursetype, commandtype
        返回值：POST数据(dict)
        最后一次修改时间：2018年6月26日 21:58:01
    """
    def generatePOSTDATA(self, course, coursetype, commandtype):
        pattern = r'<form name=.+action="(.+)" method=.+'
        obj = re.compile(pattern)
        action = obj.findall(course)
        _token = ''
        pattern = r'<form name=.+name="_token" value="(.+)"><button type.+'
        obj = re.compile(pattern)
        _token = obj.findall(course)
        pattern = r'<form name=.+name="kcxh" value="(.+)"><input type.+'
        obj = re.compile(pattern)
        kcxh = obj.findall(course)
        if commandtype == 'elect':
            postdata = {
                '_token': _token[0],
                'kcxh': kcxh[0],
                'type': coursetype,
            }
            return action[0], postdata
        elif commandtype == 'delete':
            postdata = {
                "_method": 'delete',
                '_token': _token[0],
            }
            return action[0], postdata
        else:
            return None



