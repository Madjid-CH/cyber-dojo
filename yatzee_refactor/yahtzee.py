def chance(d1, d2, d3, d4, d5):
    return sum([d1, d2, d3, d4, d5])


def yahtzee(dice):
    counts = count_frequency(dice)
    return 50 if 5 in counts else 0


def count_frequency(dice):
    counts = [0] * (len(dice) + 1)
    for die in dice:
        counts[die - 1] += 1
    return counts


def _ns(dice, n):
    return sum([die for die in dice if die == n])


def ones(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 1)


def twos(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 2)


def threes(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 3)


def fours(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 4)


def fives(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 5)


def sixes(d1, d2, d3, d4, d5):
    return _ns([d1, d2, d3, d4, d5], 6)


def pair(d1, d2, d3, d4, d5):
    counts = count_frequency([d1, d2, d3, d4, d5])
    for at in range(5, 0, -1):
        if counts[at] == 2:
            return (at + 1) * 2
    return 0


def two_pair(d1, d2, d3, d4, d5):
    counts = count_frequency([d1, d2, d3, d4, d5])
    n_pairs = 0
    score = 0
    for i in range(6):
        if counts[i] == 2:
            n_pairs += 1
            score += i + 1

    if n_pairs == 2:
        return score * 2
    else:
        return 0


def four_of_a_kind(d1, d2, d3, d4, d5):
    tallies = count_frequency([d1, d2, d3, d4, d5])
    for i in range(6):
        if tallies[i] == 4:
            return (i + 1) * 4
    return 0


def three_of_a_kind(d1, d2, d3, d4, d5):
    t = count_frequency([d1, d2, d3, d4, d5])
    for i in range(6):
        if t[i] == 3:
            return (i + 1) * 3
    return 0


def small_straight(d1, d2, d3, d4, d5):
    tallies = count_frequency([d1, d2, d3, d4, d5])
    if tallies == [1, 1, 1, 1, 1, 0]:
        return 15
    return 0


def large_straight(d1, d2, d3, d4, d5):
    tallies = count_frequency([d1, d2, d3, d4, d5])
    if tallies == [0, 1, 1, 1, 1, 1]:
        return 20
    return 0


def full_house(d1, d2, d3, d4, d5):
    dices = [d1, d2, d3, d4, d5]
    tallies = count_frequency(dices)
    if n_ple_exists(tallies, 2) and n_ple_exists(tallies, 3):
        return sum(dices)
    else:
        return 0


def n_ple_exists(tallies, n):
    tuple_exists = False
    for i in range(6):
        if tallies[i] == n:
            tuple_exists = True
    return tuple_exists
