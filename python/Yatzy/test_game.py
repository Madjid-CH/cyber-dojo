import pytest
from Yatzy.scoring import chance
from Yatzy.game import roll_dices, play_round


def test_roll_dices():
    assert len(roll_dices(5)) == 5


@pytest.fixture
def reporter():
    class Reporter:
        def __init__(self):
            self.rolls = []

        def report(self, roll):
            self.rolls.append(roll)
            print(f"Roll #{len(self.rolls)}: {roll}")

        def get_saved_dice(self):
            saved_dice = self.rolls[-1][0]
            return saved_dice

        def get_scorer(self):
            return chance

        def keep_rolling(self, i):
            return i < 2

    return Reporter()


@pytest.fixture
def fake_dice(monkeypatch):
    monkeypatch.setattr("Yatzy.game.roll_dices", lambda n: tuple(range(1, n + 1)))


def test_play_round_with_three_throws(fake_dice, reporter):
    assert play_round(reporter) == 8


def test_play_round_with_two_throws(fake_dice, reporter):
    reporter.keep_rolling = lambda i: i < 1
    assert play_round(reporter) == 11


def test_play_round_with_one_throw(fake_dice, reporter):
    reporter.keep_rolling = lambda i: i < 0
    assert play_round(reporter) == 15
