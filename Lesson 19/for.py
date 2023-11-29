list1 = [10, 20, 30, 'ASD', ('A', 'B', 'C')]

for el in list1:
    print(el)

print('-'*100)
print(range(5))

print('-'*100)
n = 5
for x in range(1, n+1):
    print('Грибы', x)

print('-'*100)
var1 = input('Введите кол-во грибов на поляне: ')
if var1.isdigit():
    var1 = int(var1)
else:
    assert False, 'Введите число!'
print('Start')
for mush_numb in range(1, var1+1):
    if mush_numb >= 30:
        print('Я устал ...')
        break
    print('Я собрал гриб номер', mush_numb)
    if 10 < mush_numb <= 30: continue
    print('Как я счастлив!')
else:
    print('Я счастливый и довольный пошел домой =)')
print('END')