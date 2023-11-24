
var1 = int(input())

if var1 == 1:
    print('Ввод единички')
elif var1 == 2:
    print('Ввод двойки')
elif var1 == 3:
    print('Ввод тройки')
else:
    print('Ввод непойми чего')

print('-'*100)

match var1:
    case 1:
        print('Ввод единички')
    case 2:
        print('Ввод двойки')
    case 3:
        print('Ввод тройки')
    case _:
        print('Ввод непойми чего')

print('-'*100)

dict1 = {1: 'Ввод единички',
         2: 'Ввод двойки',
         3: 'Ввод тройки'}

if var1 in dict1:
    print(dict1[var1])
else:
    print('Ввод непойми чего')
