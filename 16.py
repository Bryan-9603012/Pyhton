#1-1
# from datetime import datetime 
# now = datetime.now()
# print(now)
# day=now.day
# month=now.month
# year=now.year
# hour=now.hour
# minute=now.minute
# second=now.second
# timestamp=now.timestamp()
# print(day,month,year,hour,minute,second,"\n")
# print(timestamp,"\n")
# print(f"{year}-{month}-{day} {hour}:{minute}:{second}","\n")

#1-2
# from datetime import datetime 
# now = datetime.now()
# t = now.strftime("%Y-%m-%d %H:%M:%S")
# print("time:",t,"\n")
# time_one = now.strptime(t,"%Y-%m-%d %H:%M:%S")
# print("time_one:",time_one,"\n")
# time_two = now.strftime("%Y-%d-%m %H:%M:%S")
# print("time_two:",time_two,"\n")

#1-3
# from datetime import datetime 
# date_string = "2019-12-05"
# print("date_string:",date_string,"\n")
# date_object = datetime.strptime(date_string,"%Y-%m-%d")
# print("date_object:",date_object,"\n")

#1-4
# from datetime import date, datetime
# today = date(year=2024, month=6, day=15)
# new_year = date(year=2025, month=1, day=1)
# time_left = new_year - today
# t1=datetime(year=2024, month=6, day=15,hour=12,minute=0,second=0)
# t2=datetime(year=2025, month=1, day=1,hour=0,minute=0,second=0)
# time_left_2 = t2 - t1
# print("距離新年還有:", time_left_2.days, "天", time_left_2.seconds//3600, "小時", (time_left_2.seconds//60)%60, "分鐘", time_left_2.seconds%60, "秒")

#1-5
# from datetime import datetime, timedelta,timezone
# now = datetime.now(timezone.utc)

# offset = timedelta(days=1,hours=2,minutes=3,seconds=4,milliseconds=5)
# new_time = now- offset
# delta = now-datetime(1970,1,1,tzinfo=timezone.utc)
# print("從1970年1月1日到現在的總秒數:", delta.total_seconds())