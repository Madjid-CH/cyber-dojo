from functools import reduce, partial


def chance(roll):
    return sum(roll)


def yatzy(roll):
    comparison = [roll[i] == roll[i + 1] for i in range(len(roll) - 1)]
    all_equal = reduce(lambda a, b: a and b, comparison)
    return 50 if all_equal else 0


def _n_sumer(n, roll):
    return sum(filter(lambda x: x == n, roll))


ones = partial(_n_sumer, 1)
twos = partial(_n_sumer, 2)
threes = partial(_n_sumer, 3)
fours = partial(_n_sumer, 4)
fives = partial(_n_sumer, 5)
sixs = partial(_n_sumer, 6)


def pair(roll):
    pairs = _get_tuples(roll, 2)
    if len(pairs) == 0:
        return 0

    pairs = max(pairs, key=lambda x: x[0])
    return pairs[0] * 2


def two_pairs(roll):
    pairs = _get_tuples(roll, 2)
    if len(pairs) != 2:
        return 0
    else:
        return sum(map(lambda x: x[0], pairs)) * 2


def three_of_a_kind(roll):
    return _n_of_a_kind(roll, 3)


def _n_of_a_kind(roll, n):
    tuples = _get_tuples(roll, n)
    return tuples[0][0] * n if tuples else 0


def _get_tuples(roll, n):
    grouped = {i: 0 for i in range(1, 7)}
    for i in roll:
        grouped[i] += 1
    tuple_ = tuple(filter(lambda x: x[1] == n, grouped.items()))
    return tuple_


def four_of_a_kind(roll):
    return _n_of_a_kind(roll, 4)


def small_straight(roll):
    is_small_straight = tuple(roll) == tuple(range(1, 6))
    return sum(roll) if is_small_straight else 0


def large_straight(roll):
    is_large_straight = tuple(roll) == tuple(range(2, 7))
    return sum(roll) if is_large_straight else 0


def full_house(roll):
    triples = _get_tuples(roll, 3)
    pairs = _get_tuples(roll, 2)
    if not triples or not pairs:
        return 0

    return sum(roll)
