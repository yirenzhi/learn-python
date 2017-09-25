# -*- coding: utf-8 -*-
import datetime

nvyou_birth_str='09-22'
now_time = datetime.datetime.today()

nvyou_birth_str = str(now_time.year)+'-'+nvyou_birth_str

nvyou_birth = datetime.datetime.strptime(nvyou_birth_str,'%Y-%m-%d')

ditance_time =  now_time - nvyou_birth

print("女友生日距离现在还有"+str(ditance_time.days)+"天")
print("女友生日是星期"+str(nvyou_birth.weekday()+1))
