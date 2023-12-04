print(bool('ASD'))
print(bool(''))
print(bool(10))
print(bool(0))
print('-'*100)

print(5**50)
print(pow(5, 50))
print('-'*100)

print(abs(10))
print(abs(-15))
print('-'*100)

print(round(4.6666, 2))
print(round(4.4444, 2))
print('-'*100)

list1 = [1, 2, 3]
print(sum(list1))

var_int = 0
for i in list1:
    var_int += i
print(var_int)
print('-'*100)

print(min(list1))

var_min = list1[0]
for i in list1:
    if i < var_min:
        var_min = i
print(var_min)

print(max(list1))
var_max = list1[0]
for i in list1:
    if i > var_max:
        var_max = i
print(var_max)

