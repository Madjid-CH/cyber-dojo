from random import randint
from typing import Protocol

N_DICES = 5


def roll_dices(n):
    return tuple(randint(1, 6) for _ in range(n))


class Reporter(Protocol):
    def report(self, roll):
        ...

    def get_saved_dice(self)-> int:
        ...

    def get_scorer(self) -> callable:
        ...

    def keep_rolling(self, i) -> bool:
        ...


def play_round(reporter: Reporter):
    saved_dices = []
    for i in range(3):
        current_roll = play_roll(reporter, saved_dices, i)
    scorer = reporter.get_scorer()
    return scorer(list(current_roll) + saved_dices)


def play_roll(reporter, saved_dices, i):
    current_roll = roll_dices(N_DICES - len(saved_dices))
    reporter.report(current_roll)
    if reporter.keep_rolling(i):
        saved_dices.append(reporter.get_saved_dice())
    return current_roll
