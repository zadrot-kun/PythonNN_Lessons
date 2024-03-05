import random
import pytest
import datetime


def pytest_addoption(parser):
    parser.addoption(
        "--num_iter", action="store", default=1000, help="кол-во итераций тестирования"
    )

@pytest.fixture(scope='module')
def prepere_data_for_mult(pytestconfig):
    start_datetime = datetime.datetime.now()
    num_iter = int(pytestconfig.getoption('num_iter'))
    print(num_iter)
    data_for_mult = list()
    for i in range(num_iter):
        x = random.randint(0, 1000000)
        y = random.randint(0, 1000000)
        data_for_mult.append((x, y, x*y))
    end_datetime = datetime.datetime.now()
    diff = end_datetime - start_datetime
    print('Фикстура 1', diff.total_seconds())
    return data_for_mult


@pytest.fixture()
def prepere_file_data_for_mult(tmp_path, prepere_data_for_mult):
    print(tmp_path)
    start_datetime = datetime.datetime.now()
    file_path = tmp_path / 'testmult.txt'
    result_list = list()
    with open(file_path, 'w') as file:
        for line in prepere_data_for_mult:
            file.write(str(line[0]) + ' ' + str(line[1]) + '\n')
            result_list.append(line[2])
    end_datetime = datetime.datetime.now()
    diff = end_datetime - start_datetime
    print('Фикстура 2', diff.total_seconds())

    yield file_path, result_list

    open(file_path, 'w')
