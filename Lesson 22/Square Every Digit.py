def square_digits(num):
    return int(''.join(map(str, [int(x)**2 for x in list(str(num))])))