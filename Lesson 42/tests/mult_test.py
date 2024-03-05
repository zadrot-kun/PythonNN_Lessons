import pytest
from multiply_module import multiple, multiple_from_file
import datetime

iter_count_param = [1000,
                    10000,
                    100000,
                    1000000,
                    10000000]


@pytest.mark.parametrize("iter_count", iter_count_param)
def test_mult(prepere_data_for_mult, iter_count):
    start_datetime = datetime.datetime.now()
    iter_data = prepere_data_for_mult[:iter_count]
    for res in iter_data:
        assert res[2] == multiple(res[0], res[1])
    end_datetime = datetime.datetime.now()
    diff = end_datetime - start_datetime
    print('Выполнение', diff.total_seconds())

def test_file_mult(prepere_file_data_for_mult):
    start_datetime = datetime.datetime.now()
    assert prepere_file_data_for_mult[1] == multiple_from_file(prepere_file_data_for_mult[0])
    end_datetime = datetime.datetime.now()
    diff = end_datetime - start_datetime
    print('Выполнение', diff.total_seconds())