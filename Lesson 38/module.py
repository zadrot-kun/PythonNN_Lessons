

class MyException(Exception):
    def __str__(self):
        return 'Моё опасное исключение'


def func():
    print('1')
    print('2')
    print('3')
    assert 1 == 1, 'текст ошибки'
    # if 1 == 1:
    #     raise MyException('Ошибка!!!')
    print('4')
    print('5')


