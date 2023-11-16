list1 = [123, 123.123, '123', [1, 2, 3]]
list2 = list((123, 123.123, '123', [1, 2, 3]))
list3 = list('Hello')
list4 = []
list5 = list(range(-4, 4))


print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(range(-4, 4))
print('-'*100)

list6 = [0, 10, 20, 30, 40]
print(list6)
list6[0] = 1000
print(list6)
list6[1:4] = [80, 90]
print(list6)
list6[1:3] = ['Hello']
print(list6)
list6[1:2] = []
print(list6)
print('-'*100)

list7 = []
list7.append('Hello')
list7.append('world!')
print(list7)
list7.insert(1, ' ')
print(list7)
print('-'*100)

list8 = [1, 2, 0, 2, 0, 1, 3]
print(list8)
list8.remove(0)
print(list8)
list8.remove(0)
print(list8)
del list8[1:3]
print(list8)
list8.clear()
print(list8)
print('-'*100)

list9 = [10, 20, 30, 40, 50]
print(list9)
print(list9.pop())
print(list9)
print(list9.pop(1))
print(list9)
list10 = [60, 70, 80]
list9.extend(list10)
print(list9)
