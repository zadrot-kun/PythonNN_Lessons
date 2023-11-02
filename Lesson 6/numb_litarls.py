import decimal

print(1)
print(.0)
print(14e+100)
print(0b100)
print((0.1 + 0.1) / 0.3)
decimal.getcontext().prec = 3
print((decimal.Decimal(0.1) + decimal.Decimal(0.1)) / decimal.Decimal(0.3))
