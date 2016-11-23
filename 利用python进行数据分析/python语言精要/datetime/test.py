# -*- coding: utf-8 -*-
from datetime import datetime,date, time
dt = datetime(2011, 10, 29, 20, 30 )
print dt.day
print dt.minute
print dt.date()
print dt.time()

#strftime 用于将datetime格式化为字符串
print datetime.strptime('20091031','%Y%m%d')

print dt.replace(minute=0, second=0)

#两个datetime对象的差会产生一个datetime.timedelta类型：
dt2 = datetime(2011,10,29,22,30)

tdel = dt2-dt
print type(tdel)
print tdel
tdel.days=100
print tdel
#print dir(dt-dt2)

'''
2:00:00
-1 day, 22:00:00
减出的差值如果是负，后面的时候仍然会为正
'''
