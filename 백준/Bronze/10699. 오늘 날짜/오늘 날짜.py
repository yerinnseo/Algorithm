import datetime 

now = datetime.datetime.now()

print((now+datetime.timedelta(hours=9)).strftime("%Y-%m-%d"))