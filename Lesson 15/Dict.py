dict1 = {} # пустой словарь

dict2 = {'Козлов': "Эксперт", "Екатерина": "Ведущий консультант"}
print(dict2['Козлов'])

dict3 = {100: 'Сто', '200': "Двести", ('Эксперт', "Направление бизнес-анализа"): 100000}

dict4 = {'ФИО': "Козлов Артем Александрович", "Должность": "Эксперт", "Рост": 175}
dict5 = {'ФИО': "Кошелева Елена Владимировна", "Должность": "Главный консультант"}

list1 = []
list1.append(dict4)
list1.append(dict5)

print("-"*100)
for el in list1:
    if 'ФИО' in el:
        print(el['ФИО'])
    if 'Рост' in el:
        print(el['Рост'])
    print("-"*100)

for el in dict4:
    print(el)

list2 = list(dict4)
print(list2)

dict6 = dict(ФИО="Козлов Артем Александрович", Рост=175)
print(dict6)

dict7 = dict(zip(["ФИО", "Рост"],["Козлов Артем Александрович", 175]))
print(dict7)

dict8 = dict([("ФИО", "Козлов Артем Александрович"), ("Рост", 175)])
print(dict8)

dict9 = {}
dict9['ФИО'] = "Козлов Артем Александрович"
dict9['Должность'] = "Эксперт"
dict9['Рост'] = 175
print(dict9)

del dict9['ФИО']
print(dict9)

print(sorted(list1, key=lambda el: el['Должность']))
