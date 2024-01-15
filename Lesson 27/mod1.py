import mod2
from mod2 import x as mod2x

y = 15

print(mod2.x)
print(y)
print(mod2x)

print('-'*100)

def func1(z):
    y = 2
    def x():
        def f():
            pass
        return y * z
    return x

y = func1(20)
g = func1(25)
del func1
print(y())
print(g())
print(y)

print('-'*100)

y = 10
def func2():
    y = 20
    def func3():
        y = 30
        def func4():
            nonlocal y
            y *= 2
            return y
        return func4()
    return func3()

print(func2())
print(y)
