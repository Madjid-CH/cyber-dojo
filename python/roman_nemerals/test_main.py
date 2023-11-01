import pytest

from roman_nemerals.main import roman_numeral, get_higher_position


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, ""),
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (9, "IX"),
        (10, "X"),
        (11, "XI"),
        (20, "XX"),
        (30, "XXX"),
        (40, "XL"),
        (50, "L"),
        (60, "LX"),
        (70, "LXX"),
        (80, "LXXX"),
        (90, "XC"),
        (100, "C"),
        (200, "CC"),
        (300, "CCC"),
        (400, "CD"),
        (500, "D"),
        (600, "DC"),
        (700, "DCC"),
        (800, "DCCC"),
        (900, "CM"),
        (1000, "M"),
        (2000, "MM"),
        (3000, "MMM"),
        (4000, "MMMM"),
        (1990, "MCMXC"),
        (2008, "MMVIII"),
        (99, "XCIX"),
        (47, "XLVII"),
    ],
)
def test_roman_numerals(n, expected):
    assert roman_numeral(n) == expected


def test_high_roman_numerals():
    with pytest.raises(ValueError):
        roman_numeral(5000)


@pytest.mark.parametrize("n, expected", [(1, 1), (10, 10), (25168, 20000)])
def test_get_higher_position(n, expected):
    assert get_higher_position(n) == expected
