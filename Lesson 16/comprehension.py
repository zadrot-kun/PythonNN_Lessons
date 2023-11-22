dict1 = {x: x**2 for x in range(10) if x % 2 == 0}
print(dict1)

dict2 = {1: 'abc', 2: 'ABC', 3: "АБВ"}
dict3 = {x: dict2[x]*5 for x in dict2}
dict4 = {x: y*5 for x, y in dict2.items()}
print(dict3)
print(dict4)
