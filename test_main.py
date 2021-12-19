import random
import time

import pytest

from main import find_max, find_min, calc_sum, calc_mult


def random_array(size=1000):
    out = []
    for i in range(size):
        out.append(random.randint(-1000, 1000))
    return out


def run_all(array):
    find_min(array)
    find_max(array)
    calc_sum(array)
    calc_mult(array)


def test_find_max():
    array = random_array()
    _max = find_max(array)
    assert max(array) == _max
    assert find_max([]) is None


def test_find_min():
    array = random_array()
    _min = find_min(array)
    assert min(array) == _min
    assert find_min([]) is None


def test_calc_sum():
    array = random_array()
    _sum = calc_sum(array)
    assert sum(array) == _sum
    assert calc_sum([0, 1, 2, 3, 4]) == 10
    assert calc_sum([]) == 0


def test_calc_mult():
    array = [1, 2, 5, 20]
    mult = calc_mult(array)
    assert mult == 200
    assert calc_mult([]) == 0


def test_all_func_for_time():
    array_1 = random_array(10 ** 3)
    array_2 = random_array(10 ** 5)

    start_time_1 = time.time()
    run_all(array_1)
    duration_1 = time.time() - start_time_1

    start_time_2 = time.time()
    run_all(array_2)
    duration_2 = time.time() - start_time_2

    assert duration_1 < duration_2


def test_right_type():
    with pytest.raises(TypeError):
        find_min('')
    with pytest.raises(TypeError):
        find_max('')
    with pytest.raises(TypeError):
        calc_sum('')
    with pytest.raises(TypeError):
        calc_mult('')

