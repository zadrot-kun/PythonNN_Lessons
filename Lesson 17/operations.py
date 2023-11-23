var1 = 100
print(var1 == 100)

var2 = [1, 2, 3]
var3 = var2
print(var2 is var3)
var3 = [1, 2, 3]
print(var2 is var3)

print(1 in [1, 2, 3])
print(4 not in [1, 2, 3])
print('-'*100)
print(2 > 1)
print(1 == 1)
print(1 >= 1)
print(1 <= 1)
print(0 < 1)
print(0 != 1)
print('-'*100)

print(False and False)
print(True and False)
print(True and True)
print('-'*100)
print(False or False)
print(True or False)
print(True or True)
print('-'*100)
print((not False) and (not False))
print(not True and False)
print(not True and True)
print('-'*100)

print(11 or 0)
dict1 = {'a': 100, 'b': 200}
print('c' in dict1 and dict1['c'])
print('a' in dict1 and dict1['a'])
