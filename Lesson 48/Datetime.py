import datetime

var1 = datetime.date(2024, 3, 20)
print(var1)

var2 = datetime.time(8, 0, 30, 200)
print(var2)

var3 = datetime.datetime(2024, 3, 20, 8, 7, 32, 3500)
print(var3)

var4 = datetime.datetime.now()
print(var4)
var5 = datetime.datetime.now()
var6 = var5 - var4

print(var4.strftime('%y'))
