import pytest

from bowling_game.main import parse, parse_frame, parse_bonus, score_game


def perfect_game():
    result = [(10, 0)] * 10 + [(10,), (10,)]
    return "X|X|X|X|X|X|X|X|X|X||XX", result


def all_spare():
    result = [(5, 5)] * 10 + [(5,)]
    return "5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5", result


def test_parse_strike():
    assert parse_frame("X") == (10, 0)


def test_parse_spare():
    assert parse_frame("5/") == (5, 5)


def test_parse_spare_with_miss():
    assert parse_frame("-/") == (0, 10)


def test_parse_open():
    assert parse_frame("45") == (4, 5)


@pytest.mark.parametrize(
    "bonus, expected",
    [
        ("XX", ((10,), (10,))),
        ("X-", ((10,), (0,))),
        ("X5", ((10,), (5,))),
        ("55", ((5,), (5,))),
        ("5-", ((5,), (0,))),
        ("--", ((0,), (0,))),
        ("X", ((10,),)),
        ("5", ((5,),)),
        ("-", ((0,),)),
    ],
)
def test_parse_bonus(bonus, expected):
    assert parse_bonus(bonus) == expected


def test_parse_two_misses():
    assert parse_frame("--") == (0, 0)


def test_parse_one_miss():
    assert parse_frame("-4") == (0, 4)


@pytest.mark.parametrize("input_, expected", [perfect_game(), all_spare()])
def test_parse(input_, expected):
    assert parse(input_) == expected


def test_score_perfect_game():
    game, _ = perfect_game()
    assert score_game(parse(game)) == 300


def test_all_spare():
    game, _ = all_spare()
    assert score_game(parse(game)) == 150


def test_no_bonus_game():
    game = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||"
    assert score_game(parse(game)) == 90


def test_all_misses():
    game = "--|--|--|--|--|--|--|--|--|--||"
    assert score_game(parse(game)) == 0


def test_of_acceptance():
    game = "X|7/|9-|X|-8|8/|-6|X|X|X||81"
    assert score_game(parse(game)) == 167
