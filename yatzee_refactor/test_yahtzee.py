import pytest

import yahtzee


@pytest.mark.parametrize(
    "dices, expected", [((2, 3, 4, 5, 1), 15), ((3, 3, 4, 5, 1), 16)]
)
def test_chance_scores_sum_of_all_dice(dices, expected):
    actual = yahtzee.chance(*dices)
    assert expected == actual


@pytest.mark.parametrize(
    "dices, expected",
    [((4, 4, 4, 4, 4), 50), ((6, 6, 6, 6, 6), 50), ((6, 6, 6, 6, 3), 0)],
)
def test_yahtzee_scores_50(dices, expected):
    actual = yahtzee.yahtzee(dices)
    assert expected == actual


@pytest.mark.parametrize(
    "dices, expected",
    [
        ((1, 2, 3, 4, 5), 1),
        ((1, 2, 1, 4, 5), 2),
        ((6, 2, 2, 4, 5), 0),
        ((1, 2, 1, 1, 1), 4),
    ],
)
def test_1s(dices, expected):
    assert yahtzee.ones(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected", [((1, 2, 3, 2, 6), 4), ((2, 2, 2, 2, 2), 10)]
)
def test_2s(dices, expected):
    assert yahtzee.twos(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected", [((1, 2, 3, 2, 3), 6), ((2, 3, 3, 3, 3), 12)]
)
def test_3s(dices, expected):
    assert yahtzee.threes(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((4, 4, 4, 5, 5), 12), ((4, 4, 5, 5, 5), 8), ((4, 5, 5, 5, 5), 4)],
)
def test_4s(dices, expected):
    assert yahtzee.fours(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((4, 4, 4, 5, 5), 10), ((4, 4, 5, 5, 5), 15), ((4, 5, 5, 5, 5), 20)],
)
def test_5s(dices, expected):
    assert yahtzee.fives(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((4, 4, 4, 5, 5), 0), ((4, 4, 6, 5, 5), 6), ((6, 5, 6, 6, 5), 18)],
)
def test_6s(dices, expected):
    assert yahtzee.sixes(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((3, 4, 3, 5, 6), 6), ((5, 3, 3, 3, 5), 10), ((5, 3, 6, 6, 5), 12)],
)
def test_one_pair(dices, expected):
    assert yahtzee.pair(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected", [((3, 3, 5, 4, 5), 16), ((3, 3, 5, 5, 5), 0)]
)
def test_two_pair(dices, expected):
    assert yahtzee.two_pair(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((3, 3, 3, 4, 5), 9), ((5, 3, 5, 4, 5), 15), ((3, 3, 3, 3, 5), 0)],
)
def test_three_of_a_kind(dices, expected):
    assert yahtzee.three_of_a_kind(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((3, 3, 3, 3, 5), 12), ((5, 5, 5, 4, 5), 20)],
)
def test_four_of_a_kind(dices, expected):
    assert yahtzee.four_of_a_kind(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((1, 2, 3, 4, 5), 15), ((2, 3, 4, 5, 1), 15), ((1, 2, 2, 4, 5), 0)],
)
def test_small_straight(dices, expected):
    assert yahtzee.small_straight(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected",
    [((6, 2, 3, 4, 5), 20), ((2, 3, 4, 5, 6), 20), ((1, 2, 2, 4, 5), 0)],
)
def test_large_straight(dices, expected):
    assert yahtzee.large_straight(*dices) == expected


@pytest.mark.parametrize(
    "dices, expected", [((6, 2, 2, 2, 6), 18), ((2, 3, 4, 5, 6), 0)]
)
def test_full_house(dices, expected):
    assert yahtzee.full_house(*dices) == expected
