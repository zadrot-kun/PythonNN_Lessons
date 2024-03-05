def multiple(x, y):
    return x * y


def multiple_from_file(path):
    res_list = list()
    with open(path, 'r') as f:
        for line in f:
            x, y = list(map(int, line.split(' ')))
            res_list.append(multiple(x, y))
    return res_list


if __name__ == '__main__':
    print(multiple_from_file('mult.txt'))
