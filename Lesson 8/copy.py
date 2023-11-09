import copy

var1 = [10, 21, 32, [12, 13], 54, 65, 76]

var2 = var1.copy()
var1[3][0] = 'T'
var1[0] = 'W'
print(var1, var2, sep='\n')