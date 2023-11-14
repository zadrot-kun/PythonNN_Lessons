var1 = '1234'
var2 = 'asdf'
var3 = '12asd'
var4 = '12_*asd'
var5 = '1234.15'
var6 = '\u00B2'
var7 = '\u00BD'
var8 = '*a1sd'
var9 = 'ASDF'
var10 = 'a f\nf'
var11 = ' \t\n'
var12 = 'New York Times'

print('isalnum - ', var4.isalnum())
print('isalpha - ', var2.isalpha())
print('isdecimal - ', var1.isdecimal())
print('isdigit - ', var6.isdigit())
print('isnumeric - ', var7.isnumeric())
print('isidentifier - ', var8.isidentifier())
print('islower - ', var2.islower())
print('isupper - ', var9.isupper())
print('isprintable - ', var10.isprintable())
print('isspace - ', var11.isspace())
print('istitle - ', var12.istitle())
