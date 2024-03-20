import decimal

decimal.getcontext().prec = 3

var1 = 1 / 3
var2 = decimal.Decimal('1.000')
var4 = var2 / 3
print(var4)

with decimal.localcontext() as ctx:
    ctx.prec = 4
    var4 = var2 / 3
    print(var4)

with decimal.localcontext() as ctx:
    ctx.prec = 5
    var4 = var2 / 3
    print(var4)