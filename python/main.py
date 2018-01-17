from Crawler import DeanCrawler
import sys

def demo(username,password,sel_mode):
    crawler = DeanCrawler(username,password)
    if sel_mode == '0':
        LIST = crawler.InternalExamScores()
    elif sel_mode == '1':
        LIST = crawler.classtable()
    elif sel_mode == '2':
        LIST = crawler.unconfirmedScore()
    elif sel_mode == '3':
        LIST = crawler.TotalScore()
    else:
        print("没有这个功能")
        sys.exit(0)
    return LIST


