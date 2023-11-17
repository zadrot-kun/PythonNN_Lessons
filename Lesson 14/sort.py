list1 = [['Артем', 3], ["Елена", 2], ["Андрей", 1]]
list2 = ['a', 'c', 'b', 'A', 'C', 'B']

list1.sort(key=lambda el: el[1])
list2.sort()
list4 = ['a', 'c', 'b', 'A', 'C', 'B']
list4.reverse()

print(list1)
print(list2)
print(list4)

list3 = [1, 3, 4, 2]
sorted_list1 = sorted(list1, key=lambda el: el[1], reverse=True)
print(sorted_list1)
sorted_list2 = list(reversed(list3))
print(sorted_list2)

