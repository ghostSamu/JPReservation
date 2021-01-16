import subprocess

from scrapy.cmdline import execute
import sys
import os
import schedule
import datetime
import time
import subprocess


# 第三个参数是：爬虫程序名
def start_scrapy():
    # try:
        # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        # env = os.environ.copy()
        # execute(['scrapy', 'crawl','appointement'])
        subprocess.Popen(['scrapy', 'crawl','appointement'])

    # except Exception as e:
    #     print(e)

# schedule.every(1).minutes.do(start_scrapy) # 每30分钟执行一次,注意这里的参数传递的是函数名,不要加括号
#schedule.every().hour.do(job)#每隔一小时执行一次任务
#schedule.every().day.at("23:30").do(job)#每天的23:30执行一次任务
#schedule.every().monday.do(job)#每周一的这个时候执行一次任务
#schedule.every().wednesday.at("23:30").do(job)#每周三23:30执行一次任务

def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec

def compare_time(startTime,endTime):
    now = datetime.datetime.now ()
    # print(now)
    d_start = datetime.datetime.strptime (startTime, '%Y-%m-%d %H:%M:%S')
    # print(d_start)
    d_end = datetime.datetime.strptime (endTime, '%Y-%m-%d %H:%M:%S')
    # print(d_end)
    result = (d_start<=now) and (d_end>=now)
    return result

if __name__ == '__main__':

    while True:
        result = compare_time('2021-01-15 00:00:00', '2021-01-15 11:05:00')
        print(result)
        if result:
            second = sleeptime(0, 0, 30)
            time.sleep(second)
            start_scrapy()
        else:
            break

