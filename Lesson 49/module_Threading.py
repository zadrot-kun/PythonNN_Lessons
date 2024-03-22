import threading

def simple_math():
    with open('simple_math.txt', 'w') as f:
        f.write('4')

def hard_math(counter):
    result_value = 1
    for x in range(1, 10**counter):
        result_value *= x
    with open('hard_math.txt', 'w') as f:
        f.write(str(result_value))


threading.Thread(target=hard_math, name="hard_math", args=(5, ), daemon=False).start()
print('simple_math', simple_math())

def test():
    await
