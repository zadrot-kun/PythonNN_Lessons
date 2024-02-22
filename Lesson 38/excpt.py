
var0 = 10
var1 = 1

try:
    var0 = 5
    var1 = 100 / 0
except ZeroDivisionError as expt:
    print(dir(expt))
    print(expt.args)
    var1 = 100 / 0
    print(var0)
else:
    print('ошибка не произошла')
finally:
    print('finally')

print(var0, var1)
