from python.Crawler import DeanCrawler
import sys
if __name__ == '__main__':
    crawler = DeanCrawler(sys.argv[1],sys.argv[2])
    print('综合成绩单\n' + str(crawler.TotalScore()))
    print('待确认成绩单\n' + str(crawler.unconfirmedScore()))
    print('课程表数据\n' + str(crawler.classtable()))
    print('国家成绩单\n' + str(crawler.InternalExamScores()))