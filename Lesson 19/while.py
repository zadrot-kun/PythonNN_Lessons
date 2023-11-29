var1 = input('Введите кол-во грибов на поляне: ')
if var1.isdigit():
    var1 = int(var1)
else:
    assert False, 'Введите число!'


print('Start')
mush_numb = 0
while mush_numb <= var1:
    mush_numb = mush_numb + 1
    if mush_numb >= 30:
        print('Я устал ...')
        break
    print('Я собрал гриб номер', mush_numb)
    if 10 < mush_numb <= 30: continue
    print('Как я счастлив!')
else:
    print('Я счастливый и довольный пошел домой =)')
print('END')

print('-'*100)
mush_numb = 0
while True:
    mush_numb = mush_numb + 1
    print(mush_numb)
    if mush_numb >= var1: break
