dict1 = {'ФИО': "Козлов Артем Александрович", "Должность": "Эксперт", "Рост": 175}


print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

dict2 = dict1.copy()
dict2['Рост'] = 150
print(dict1)
print(dict2)

dict2.clear()
print(dict2)

dict3 = {'ФИО': "Козлов Артем Александрович", 'Образование': "Высшее"}
dict3.update(dict1)
print(dict3)

print('ФИО' in dict1)
print(dict1.get('ФИО', 0))

print(dict3)
print(dict3.pop('Образование', 0))
print(dict3)

print(dict3)
print(dict3.setdefault('Рост__', 190))
print(dict3)
print(dict3.popitem())
print(dict3)
