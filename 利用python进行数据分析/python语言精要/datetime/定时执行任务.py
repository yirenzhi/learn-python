# -*- coding: utf-8 -*-
import datetime
import time

sched_time = datetime.datetime(2017,9,25,14,16,0)

while True:
    now_time = datetime.datetime.now()
    if sched_time<now_time<sched_time+datetime.timedelta(seconds=1):
        print('its time')
        sched_time+=datetime.timedelta(minutes=1)
    time.sleep(0.1)
