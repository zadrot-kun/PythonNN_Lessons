import random
import pytest


@pytest.fixture()
def prepere_data_for_mult():
    data_for_mult = list()
    for i in range(1000):
        x = random.randint(0, 1000000)
        y = random.randint(0, 1000000)
        data_for_mult.append((x, y, x*y))
    return data_for_mult

