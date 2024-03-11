class Human:

    def __init__(self, name, age):
        self.set_age(age)
        self.name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    age = property(get_age, set_age)



human1 = Human('Николай', 45)
human2 = Human('Ирина', 32)

print(human1.age)
print(human2.age)
print(Human.age)

human1.age = 58
human2.age = 62
# Human.age = 30

print('-'*100)
print(human1.age)
print(human2.age)
print(Human.age)

