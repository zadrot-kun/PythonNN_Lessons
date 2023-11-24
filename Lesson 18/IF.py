print(None)

var1 = int(input())

if var1 == 1:
    print('Ввод единички')
elif ((var1 < 10) and
      (var1 % 2 == 0)):
    print('Ввод меньше десяти и значение четное')
else:
    print('Ввод больше десяти или значение нечетное')

print('end')

print('one') if var1 == 1 else print('not one')
