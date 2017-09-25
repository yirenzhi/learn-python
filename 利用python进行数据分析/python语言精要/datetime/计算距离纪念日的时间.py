#encoding=utf-8
from datetime import datetime, date
import time
dt = datetime(2016,02,25)
time_now = time.localtime()
dt_now = datetime(time_now.tm_year,time_now.tm_mon,time_now.tm_mday)

dt_change = dt_now - dt
print "我们在一起时间是：2016-02-25"
print "当前时间是："+time.strftime('%Y-%m-%d %X', time.localtime())
print '我们在一起已经'+str(dt_change.days)+'天'
