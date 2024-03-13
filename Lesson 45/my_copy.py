import copy

var1 = [1, [10, 20, 30], 3]
var2 = copy.deepcopy(var1)

print(var1, var2)

print('-'*100)

var1[1][0] = 100
print(var1, var2)

print('\n\n\n\n\n')
