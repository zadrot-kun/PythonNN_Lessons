a = 'Hello'
b = 'world!'

print(a, b)
print('111')
print('-'*100)



def local_print(*params, end='\n', sep=' ', **dict_input):
    for par in params:
        print(par, end='')
        print(sep, end='')
    for el in dict_input:
        print()
        print(el, '-', dict_input[el], end='')
    print(end, end='')

local_print(a, b, pram1=123, pram2=456)
print('111')

