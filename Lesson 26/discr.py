# X*a**2 + Y*a + Z = 0

def kvadr(X, Y, Z):
    D = Y**2 - 4*X*Z
    x1 = (-Y + D**0.5) / (2 * X)
    x2 = (-Y - D**0.5) / (2 * X)
    return x1, x2

x1, x2 = kvadr(2, 2, -3)
print(x1, x2)
