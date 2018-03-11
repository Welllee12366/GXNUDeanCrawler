from Crawler import DeanCrawler

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
    elif sel_mode == '4':
        LIST = crawler.getName()
    else:
        return("没有这个功能")
    return LIST

