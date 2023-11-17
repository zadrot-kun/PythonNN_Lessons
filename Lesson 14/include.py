list1 = [1, 2, 3, 4, 5, 6]

new_list1 = [str(el * 10) for el in list1 if el < 4]
print(new_list1)

list2 = [['Козлов', 'Артем'], ['Ксенофонтов', 'Андрей'], ['Кошелева', 'Елена']]
new_list2 = [f'Добро пожаловать! Уважаемый {x[1]} {x[0]}!!!' for x in list2]
new_list3 = [f'Добро пожаловать! Уважаемый {y} {x}!!!' for x, y in list2]

print(new_list2)
print(new_list3)
