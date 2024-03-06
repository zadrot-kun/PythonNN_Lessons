
class Class1:
    def __call__(self, *args, **kwargs):
        return int(args[0])

obj1 = Class1()

# print(obj1('позиция 1', 'позиция 2', arg1='аргумент 1', arg2='аргумент 2'))

list1 = ['123', '234', '345']
print(list1)
print(list(map(int, list1)))
print(list(map(obj1, list1)))

print('-'*100)

class Class2:
    def __getattr__(self, item):
        if item == 'attr1':
            return 1
        elif item == 'attr2':
            return 2
        else:
            return 3

    def __init__(self, attr1):
        self.attr1 = attr1

obj2 = Class2('999')
print(obj2.attr1)
print(obj2.attr2)
print(obj2.attr10)
print(obj2.asd)
print(obj2.aaaaaaaasssssssssssdddddddddd)
