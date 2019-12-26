# -*- coding:utf-8 -*-
"""
    这是一个Demo,可以测试退选课功能，后期会删除。
                    PowerBy WellLee
        最后一次修改时间：2018年6月26日 21:58:01
"""
from Crawler import DeanCrawler
import json

b = DeanCrawler('201912300205','gw100217') # 登陆操作，自行修改
"""
    以下操作为：
    1、获取当前选修课程列表
    2、选择第一门课进行测试操作
"""
text = b.getcourseJSON('http://172.16.130.20/dean/student/selcourse/listing/require/', '3')
text = json.loads(text)
data = text['data']
a = []
for i in data:
    a.append(i['action'])
firstLesson = a[0]
print(firstLesson)
"""
    以下操作为：
    1、生成退/选课数据，调整b.generatePOSTDATA中第三个参数动态生成退/选课数据 其中delete代表退，elect代表选择。
    2、调用退/选课方法进行退选课操作
"""
url, postdata = b.generatePOSTDATA(firstLesson, 'require', 'elect')
c = b.e_dcourse(url, postdata)
print(c.read())
pass