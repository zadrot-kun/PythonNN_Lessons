var1 = [x for x in range(5)]
var2 = (x for x in range(5))

print(var1)
print(var2)

print('-'*100)
for x in var1:
    print(x)

print('-'*100)
for x in var2:
    print(x)

print('-'*100)
for x in var2:
    for y in var2:
        print(x, y)

print('-'*100)
iter1 = iter(var1)
iter2 = iter(var1)

print('x:', next(iter1))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
try:
    print('y:', next(iter2))
except StopIteration:
    iter2 = iter(var1)
print('x:', next(iter1))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))

print('-'*100)
def func_gen():
    x = 0
    while True:
        yield x
        x += 1
        if x == 5:
            break

iter1 = func_gen()
iter2 = func_gen()

print('x:', next(iter1))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
try:
    print('y:', next(iter2))
except StopIteration:
    iter2 = iter(var1)
print('x:', next(iter1))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))
print('y:', next(iter2))