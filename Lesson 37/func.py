import functools

input_data = ['1', '2', '3']

int_input_data1 = []
for x in input_data:
    int_input_data1.append(int(x))

int_input_data2 = [int(x) for x in input_data]

int_input_data3 = list(map(int, input_data))

int_input_data4 = map(int, input_data)

print('-'*100)

sum1 = sum(int_input_data4)
sum2 = sum([3, 3, 3])

input_data2 = ['1', '-2', '3', '-4']

sum3 = functools.reduce(lambda a, b: a if b < 0 else a + b, list(map(int, input_data2)))
sum4 = sum([int(x) for x in input_data2 if int(x) > 0])

print('-'*100)

res_list1 = list(filter(lambda a: True if a > 0 else False, map(int, input_data2)))
res_list2 = [int(x) for x in input_data2 if int(x) > 0]

print('-'*100)

res_list3 = list(enumerate(input_data2))

print('-'*100)

dict1 = {
         'a': (0, 0, 4),
         'b': (1, 0, 2),
         'c': (0, 1, 0),
         }

res_list4 = sorted(dict1, key=lambda a: dict1[a][2])

print('-'*100)

input_data3 = [int, int, float]

res_list5 = list(zip(input_data3, input_data2))
res_list6 = []
for x in res_list5:
    res_list6.append(x[0](x[1]))


print('-'*100)