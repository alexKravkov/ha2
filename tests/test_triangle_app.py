import pytest

from Models.result_model import Res
from main import check_triangle_type


def test_scalene():
    exp = Res(0, "Scalene Triangle", "")
    res = check_triangle_type(1, 2, 3)
    act = Res.from_dict(res)
    assert act == exp


def test_isosceles():
    exp = Res(0, "Isosceles Triangle", "")
    res = check_triangle_type(1, 2, 2)
    act = Res.from_dict(res)
    assert act == exp


def test_equilateral():
    exp = Res(0, "Equilateral Triangle", "")
    res = check_triangle_type(2, 2, 2)
    act = Res.from_dict(res)
    assert act == exp


def test_large_int():
    exp = Res(0, "Equilateral Triangle", "")
    res = check_triangle_type(9223372036854775807, 9223372036854775807, 9223372036854775807)
    act = Res.from_dict(res)
    assert act == exp


def test_int_zero():
    exp = Res(1, "", "Invalid value")
    res = check_triangle_type(0, 2, 3)
    act = Res.from_dict(res)
    assert act == exp


def test_negative_int():
    exp = Res(1, "", "Invalid value")
    res = check_triangle_type(-5, 2, 3)
    act = Res.from_dict(res)
    assert act == exp


def test_missing_values():
    with pytest.raises(Exception) as e_info:
        check_triangle_type(5, 2)


def test_wrong_type_of_values():
    exp = Res(1, "", "Invalid value")
    res = check_triangle_type(5, 2, 'wow')
    act = Res.from_dict(res)
    assert act == exp


def test_special_chars():
    exp = Res(1, "", "Invalid value")
    res = check_triangle_type(5, '#', '@')
    act = Res.from_dict(res)
    assert act == exp


def test_floating_point_values():
    exp = Res(1, "", "Invalid value")
    res = check_triangle_type(5.0, 1, 1)
    act = Res.from_dict(res)
    assert act == exp


