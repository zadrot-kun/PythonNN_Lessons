set1 = {1, 2, 3, 1, 2, 3, 5}
print(set1)

set2 = set([1, 1, 2, 3, 4])
print(set2)

print(set2 & set1)
print(set2 - set1)
print(set1 - set2)
print(set1 | set2)
print(set1 ^ set2)
print(set1 > set2)

set4 = set('Hello')
print(set4)
print('H' in set4)

print('-'*100)
set3 = set()
print(type(set3))
set3.add(1)
set3.add(8)
print(set3)
print(set3.intersection([1, 2, 3]))
set3.remove(1)
print(set3)

