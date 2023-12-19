list1 = [('Артем', 65), ('Игорь', 22), ('Павел', 45)]
print(list1)


def get_age(human):
    return human[1]


list2 = sorted(list1, key=get_age, reverse=True)
print(list2)
list3 = sorted(list1, key=lambda x: x[1], reverse=True)
print(list3)

func2 = lambda x: x[1]
list4 = sorted(list1, key=func2, reverse=True)
print(list4)
