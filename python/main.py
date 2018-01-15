from Crawler import DeanCrawler
import sys
def displayList(LIST):
    for i in LIST:
        print(i)
if __name__ == '__main__':
    crawler = DeanCrawler(sys.argv[1],sys.argv[2])
    if sys.argv[3] == '0':
        LIST = crawler.InternalExamScores()
    elif sys.argv[3] == '1':
        LIST = crawler.classtable()
    elif sys.argv[3] == '2':
        LIST = crawler.unconfirmedScore()
    elif sys.argv[3] == '3':
        LIST = crawler.TotalScore()
    else:
        print("没有这个功能")
        sys.exit(0)
    displayList(LIST)