import pytest
from multiply_module import multiple


def test_mult(prepere_data_for_mult):
    for res in prepere_data_for_mult:
        print(res)
        assert res[2] == multiple(res[0], res[1])
