import time
import datetime

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))

dtn = datetime.datetime.now()
print(dtn)
print(dtn.second)
print('year:{},month:{},day:{}'.format(dtn.year,dtn.month,dtn.day))
print('hour:{},minute:{},second:{}'.format(dtn.hour,dtn.minute,dtn.second))
print('year:{},month:{},day:{} hour:{},minute:{},second:{}'
      .format(dtn.year,dtn.month,dtn.day,dtn.hour,dtn.minute,dtn.second))

dtn = datetime.datetime(2017,4,15,22,20,30)
print('year:{},month:{},day:{} hour:{},minute:{},second:{}'
      .format(dtn.year,dtn.month,dtn.day,dtn.hour,dtn.minute,dtn.second))

delta = datetime.timedelta(weeks=1,days=1,hours=5,minutes=30,seconds=8)
print(delta.days,delta.seconds)
print(str(delta))

dtn = datetime.datetime.now()
print(dtn.strftime('%Y/%m/%d %H:%M:%S'))
print(dtn.strftime('%I:%M %p'))
print(dtn.strftime("%B of %y"))