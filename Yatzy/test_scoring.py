import pytest

from Yatzy.scoring import *


def test_chance():
    roll = (1, 1, 3, 3, 6)
    assert chance(roll) == 14


@pytest.mark.parametrize(
    "roll, score", [((1, 1, 1, 1, 1), 50),
                    ((5, 5, 5, 5, 5), 50),
                    ((1, 1, 1, 2, 1), 0)]
)
def test_yatzy(roll, score):
    assert yatzy(roll) == score


def test_ones():
    roll = (1, 1, 3, 3, 6)
    assert ones(roll) == 2


def test_twos():
    roll = (1, 1, 3, 3, 6)
    assert twos(roll) == 0


@pytest.mark.parametrize(
    "roll, score",
    [
        ((3, 3, 3, 4, 4), 8),
        ((1, 1, 6, 2, 6), 12),
        ((3, 3, 3, 4, 1), 0),
        ((3, 3, 3, 3, 1), 0),
    ],
)
def test_pair(roll, score):
    assert pair(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((1, 1, 2, 3, 3), 8),
        ((1, 1, 2, 3, 4), 0),
        ((1, 1, 2, 2, 2), 0),
    ],
)
def test_two_pairs(roll, score):
    assert two_pairs(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((3, 3, 3, 4, 5), 9),
        ((3, 3, 4, 5, 6), 0),
        ((3, 3, 3, 3, 1), 0),
    ],
)
def test_three_of_a_kind(roll, score):
    assert three_of_a_kind(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((2, 2, 2, 2, 5), 8),
        ((2, 2, 2, 5, 5), 0),
        ((2, 2, 2, 2, 2), 0),
    ],
)
def test_four_of_a_kind(roll, score):
    assert four_of_a_kind(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((1, 2, 3, 4, 5), 15),
        ((2, 2, 2, 5, 5), 0),
        ((2, 2, 2, 2, 2), 0),
    ],
)
def test_small_straight(roll, score):
    assert small_straight(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((2, 3, 4, 5, 6), 20),
        ((2, 2, 2, 5, 5), 0),
        ((2, 2, 2, 2, 2), 0),
    ],
)
def test_large_straight(roll, score):
    assert large_straight(roll) == score


@pytest.mark.parametrize(
    "roll, score",
    [
        ((1, 1, 2, 2, 2), 8),
        ((2, 2, 3, 3, 4), 0),
        ((4, 4, 4, 4, 4), 0),
        ((3, 3, 3, 4, 5), 0),
    ],
)
def test_full_house(roll, score):
    assert full_house(roll) == score
