from statsapi import operation
import pytest


@pytest.mark.skip
def test_op_mean():
    operation.op_mean([1, 2, 3, 4]) == pytest.approx(2.5)


def test_op_max():
    # Como é um valor inteiro, não preciso usar o approx.
    operation.op_max([1, 2, 3, 4]) == 4


def test_op_min():
    # Como é um valor inteiro, não preciso usar o approx.
    operation.op_min([1, 2, 3, 4]) == 1


@pytest.mark.parametrize("data, expected_mean", [([1, 2, 3], 2), ([1, 2, 3, 4], 2.5)])
def test_op_mean_parametrized(data, expected_mean):
    assert operation.op_mean(data) == pytest.approx(expected_mean)
