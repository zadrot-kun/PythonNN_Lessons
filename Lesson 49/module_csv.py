import csv

var1 = csv.reader(open('test.csv'))
for x in var1:
    print(x)

var2 = csv.DictReader(open('test.csv'))
for row in var2:
    print('header:', row['header'], ', debet: ', row['debet'], ', credit: ', row['credit'])
