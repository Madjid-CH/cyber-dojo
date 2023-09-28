import pytest

from hiker import *


def example1():
    input = "Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH"
    output = "White wins - high card: Ace"
    return input, output


def example2():
    input = "Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S"
    output = "Black wins - full house"
    return input, output


def example3():
    input = "Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH"
    output = "Black wins - high card: 9"
    return input, output


def example4():
    input = "Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH"
    output = "Tie"
    return input, output


def test_parse_input():
    input, _ = example1()
    assert parse_input(input) == {
        "Black": ["2H", "3D", "5S", "9C", "KD"],
        "White": ["2C", "3H", "4S", "8C", "AH"],
    }


def test_count_same_suit():
    hand = ["2H", "3H", "5H", "9H", "KH"]
    assert count_highest_same_suit(hand) == 5


@pytest.mark.parametrize(
    "hand, n, expected",
    [
        (
            ["2H", "2D", "2S", "2C", "3H"],
            4,
            ["2H", "2D", "2S", "2C"],
        ),
        (
            ["2H", "2D", "2S", "3C", "3H"],
            3,
            ["2H", "2D", "2S"],
        ),
        (
            ["AC", "AH", "5S", "TC", "KD"],
            2,
            ["AC", "AH"],
        ),
    ],
)
def test_get_same_highest_n_cards(hand, n, expected):
    assert get_same_highest_n_cards(hand, n) == expected


def test_straight_flush_tie():
    black_hand = ["2H", "3H", "4H", "5H", "6H"]
    white_hand = ["2C", "3C", "4C", "5C", "6C"]
    assert straight_flush(black_hand, white_hand) == ("Tie", "6")


@pytest.mark.parametrize(
    "values, expected",
    [
        (["2", "3", "4", "5", "6"], 5),
        (["2", "3", "4", "5", "7"], 4),
        (["1", "3", "4", "5", "8"], 3),
        (["2", "3", "K", "5", "9"], 2),
        (["2", "4", "9", "T", "K"], 1),
    ],
)
def test_match_consecutive_values(values, expected):
    assert match_consecutive_values(values) == expected


def test_highest_consecutive_value():
    hand = ["2H", "3H", "5S", "9H", "KH"]
    assert highest_consecutive_value(hand) == 2


def test_straight_flush_black_wins():
    black_hand = ["2H", "3H", "4H", "5H", "6H"]
    white_hand = ["1C", "2C", "3C", "4C", "5C"]
    assert straight_flush(black_hand, white_hand) == ("Black", "6")


def test_straight_flush_white_wins():
    black_hand = ["2H", "3H", "4H", "5H", "6H"]
    white_hand = ["3C", "4C", "5C", "6C", "7C"]
    assert straight_flush(black_hand, white_hand) == ("White", "7")


def test_four_of_a_kind_tie():
    black_hand = ["2H", "2D", "2S", "2C", "6H"]
    white_hand = ["2C", "2H", "2S", "2D", "7C"]
    assert four_of_a_kind(black_hand, white_hand) == ("Tie", "2")


def test_four_of_a_kind_black_wins():
    black_hand = ["AC", "AH", "AS", "AD", "7C"]
    white_hand = ["2H", "2D", "2S", "2C", "6H"]
    assert four_of_a_kind(black_hand, white_hand) == ("Black", "A")


def test_four_of_a_kind_white_wins():
    black_hand = ["2H", "2D", "2S", "2C", "6H"]
    white_hand = ["AC", "AH", "AS", "AD", "7C"]
    assert four_of_a_kind(black_hand, white_hand) == ("White", "A")


def test_full_house_tie():
    black_hand = ["2H", "2D", "2S", "KC", "KH"]
    white_hand = ["2C", "2H", "2S", "KD", "KC"]
    assert full_house(black_hand, white_hand) == ("Tie", "2")


def test_full_house_black_wins():
    black_hand = ["AC", "AH", "AS", "KD", "KH"]
    white_hand = ["2H", "2D", "2S", "KC", "KH"]
    assert full_house(black_hand, white_hand) == ("Black", "A")


def test_full_house_white_wins():
    black_hand = ["2H", "2D", "2S", "KC", "KH"]
    white_hand = ["JC", "JH", "JS", "KD", "KH"]
    assert full_house(black_hand, white_hand) == ("White", "J")


def test_flush_tie():
    black_hand = ["2H", "3H", "5H", "9H", "KH"]
    white_hand = ["2C", "3C", "5C", "9C", "KC"]
    assert flush(black_hand, white_hand) == ("Tie", "2")


def test_flush_black_wins():
    black_hand = ["2H", "3H", "5H", "9H", "KH"]
    white_hand = ["2C", "3C", "5C", "9C", "QC"]
    assert flush(black_hand, white_hand) == ("Black", "K")


def test_flush_white_wins():
    black_hand = ["2H", "3H", "5H", "9H", "KH"]
    white_hand = ["2C", "3C", "5C", "9C", "AC"]
    assert flush(black_hand, white_hand) == ("White", "A")


def test_high_card_tie():
    black_hand = ["2H", "3H", "5H", "9H", "KH"]
    white_hand = ["2C", "3C", "5C", "9C", "KC"]
    assert high_card(black_hand, white_hand) == ("Tie", "2")


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["2H", "3H", "5H", "9S", "KD"],
            ["2H", "3C", "5D", "9C", "QH"],
            ("Black", "K"),
        ),
        (
            ["2H", "3H", "5H", "9S", "KD"],
            ["2H", "3C", "5D", "8C", "KH"],
            ("Black", "9"),
        ),
        (
            ["2H", "3H", "5H", "8S", "KD"],
            ["2H", "3C", "4D", "8C", "KH"],
            ("Black", "5"),
        ),
        (
            ["2H", "3H", "4H", "8S", "KD"],
            ["2H", "2C", "4D", "8C", "KH"],
            ("Black", "3"),
        ),
        (
            ["3D", "3H", "4H", "8S", "KD"],
            ["2H", "3C", "4D", "8C", "KH"],
            ("Black", "3"),
        ),
    ],
)
def test_high_card_black_wins(black_hand, white_hand, expected):
    assert high_card(black_hand, white_hand) == expected


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["2H", "3C", "5D", "9C", "QH"],
            ["2H", "3H", "5H", "9S", "KD"],
            ("White", "K"),
        ),
        (
            ["2H", "3C", "5D", "8C", "KH"],
            ["2H", "3H", "5H", "9S", "KD"],
            ("White", "9"),
        ),
        (
            ["2H", "3C", "4D", "8C", "KH"],
            ["2H", "3H", "5H", "8S", "KD"],
            ("White", "5"),
        ),
        (
            ["2H", "2C", "4D", "8C", "KH"],
            ["2H", "3H", "4H", "8S", "KD"],
            ("White", "3"),
        ),
        (
            ["2H", "3C", "4D", "8C", "KH"],
            ["3D", "3H", "4H", "8S", "KD"],
            ("White", "3"),
        ),
    ],
)
def test_high_card_white_wins(black_hand, white_hand, expected):
    assert high_card(black_hand, white_hand) == expected


def test_straight_tie():
    black_hand = ["2H", "3H", "4D", "5H", "6S"]
    white_hand = ["2C", "3D", "4C", "5C", "6D"]
    assert straight(black_hand, white_hand) == ("Tie", "2")


def test_straight_black_wins():
    black_hand = ["3C", "4D", "5C", "6C", "7D"]
    white_hand = ["2H", "3H", "4D", "5H", "6S"]
    assert straight(black_hand, white_hand) == ("Black", "7")


def test_straight_white_wins():
    black_hand = ["2H", "3H", "4D", "5H", "7S"]
    white_hand = ["3C", "4D", "5C", "6C", "7D"]
    assert straight(black_hand, white_hand) == ("White", "6")


def test_three_of_a_kind_tie():
    black_hand = ["2H", "2D", "2S", "KC", "AH"]
    white_hand = ["2C", "2H", "2S", "7D", "5C"]
    assert three_of_a_kind(black_hand, white_hand) == ("Tie", "2")


def test_three_of_a_kind_black_wins():
    black_hand = ["AC", "AH", "AS", "6D", "KH"]
    white_hand = ["2H", "2D", "2S", "3C", "AH"]
    assert three_of_a_kind(black_hand, white_hand) == ("Black", "A")


def test_three_of_a_kind_white_wins():
    black_hand = ["2H", "2D", "2S", "3C", "AH"]
    white_hand = ["AC", "AH", "AS", "6D", "KH"]
    assert three_of_a_kind(black_hand, white_hand) == ("White", "A")


def test_two_pairs_tie():
    black_hand = ["2H", "2D", "3S", "3C", "AD"]
    white_hand = ["2C", "2H", "3S", "3C", "AH"]
    assert two_pairs(black_hand, white_hand) == ("Tie", "A")


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["2H", "2D", "5S", "5C", "AD"],
            ["2C", "2H", "3S", "3C", "KH"],
            ("Black", "5"),
        ),
        (
            ["3H", "3D", "5S", "5C", "AD"],
            ["2C", "2H", "5S", "5C", "KH"],
            ("Black", "3"),
        ),
        (
            ["3H", "3D", "AS", "AC", "QD"],
            ["3C", "3H", "AS", "AC", "TH"],
            ("Black", "Q"),
        ),
    ],
)
def test_two_pairs_black_wins(black_hand, white_hand, expected):
    assert two_pairs(black_hand, white_hand) == expected


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["2C", "2H", "3S", "3C", "KH"],
            ["2H", "2D", "5S", "5C", "AD"],
            ("White", "5"),
        ),
        (
            ["2C", "2H", "5S", "5C", "KH"],
            ["3H", "3D", "5S", "5C", "AD"],
            ("White", "3"),
        ),
        (
            ["3C", "3H", "AS", "AC", "TH"],
            ["3H", "3D", "AS", "AC", "QD"],
            ("White", "Q"),
        ),
    ],
)
def test_two_pairs_white_wins(black_hand, white_hand, expected):
    assert two_pairs(black_hand, white_hand) == expected


def test_pair_tie():
    black_hand = ["2H", "2D", "5S", "TC", "KD"]
    white_hand = ["2C", "2H", "5D", "TH", "KH"]
    assert pair(black_hand, white_hand) == ("Tie", "5")


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["AC", "AH", "5S", "TC", "KD"],
            ["2C", "2H", "5D", "TH", "KH"],
            ("Black", "A"),
        ),
        (
            ["AC", "AH", "KS", "TC", "QD"],
            ["AC", "AH", "5D", "TH", "5H"],
            ("Black", "K"),
        ),
        (
            ["AC", "AH", "KS", "TC", "QD"],
            ["AC", "AH", "KD", "9H", "5H"],
            ("Black", "Q"),
        ),
        (
            ["AC", "AH", "KS", "TC", "JD"],
            ["AC", "AH", "KD", "TH", "5H"],
            ("Black", "J"),
        ),
    ],
)
def test_pair_black_wins(black_hand, white_hand, expected):
    assert pair(black_hand, white_hand) == expected


@pytest.mark.parametrize(
    "black_hand, white_hand, expected",
    [
        (
            ["2C", "2H", "5D", "TH", "KH"],
            ["AC", "AH", "5S", "TC", "KD"],
            ("White", "A"),
        ),
        (
            ["AC", "AH", "5D", "TH", "5H"],
            ["AC", "AH", "KS", "TC", "QD"],
            ("White", "K"),
        ),
        (
            ["AC", "AH", "KD", "9H", "5H"],
            ["AC", "AH", "KS", "TC", "QD"],
            ("White", "Q"),
        ),
        (
            ["AC", "AH", "KD", "TH", "5H"],
            ["AC", "AH", "KS", "TC", "JD"],
            ("White", "J"),
        ),
    ],
)
def test_pair_white_wins(black_hand, white_hand, expected):
    assert pair(black_hand, white_hand) == expected


@pytest.mark.parametrize(
    "hand, category",
    [
        (["2H", "3H", "4H", "5H", "6H"], "straight flush"),
        (["AC", "AH", "AS", "AD", "7H"], "four of a kind"),
        (["2H", "2D", "2S", "KC", "KH"], "full house"),
        (["2H", "3H", "5H", "9H", "KH"], "flush"),
        (["2H", "3H", "4D", "5H", "6S"], "straight"),
        (["2H", "2D", "2S", "KC", "AH"], "three of a kind"),
        (["2H", "2D", "3S", "3C", "AD"], "two pairs"),
        (["2H", "2D", "5S", "TC", "KD"], "pair"),
        (["2H", "3D", "5S", "9C", "KD"], "high card"),
    ],
)
def test_hand_category(hand, category):
    assert hand_category(hand) == category


@pytest.mark.parametrize(
    "input, output", [example1(), example2(), example3(), example4()]
)
def test_poker(input, output):
    assert poker(input) == output
