from more_itertools import flatten

N_PINS = 10


def parse(input_):
    frames, bonus = input_.split("||")
    frames = frames.split("|")
    scores = [parse_frame(frame) for frame in frames]
    if bonus:
        scores.extend(parse_bonus(bonus))
    return scores


def parse_bonus(bonus):
    result = []
    for b in bonus:
        if b == "X":
            result.append((10,))
        elif b == "-":
            result.append((0,))
        else:
            result.append((int(b),))
    return tuple(result)


def parse_frame(frame: str) -> tuple:
    if is_strike_str(frame):
        return N_PINS, 0
    elif is_spare_str(frame):
        first_throw = int(frame[0]) if not is_miss_str(frame[0]) else 0
        return first_throw, N_PINS - first_throw
    else:
        first_throw = int(frame[0]) if not is_miss_str(frame[0]) else 0
        second_throw = int(frame[1]) if not is_miss_str(frame[1]) else 0
        return first_throw, second_throw


def is_miss_str(throw):
    return throw == "-"


def is_strike_str(frame):
    return frame == "X"


def is_spare_str(frame):
    return frame.endswith("/")


def score_game(frames):
    score = 0
    game_length = 10
    for i in range(game_length):
        if is_strike(frames[i]):
            score += N_PINS + strike_bonus(frames, i)
        elif is_spare(frames[i]):
            score += N_PINS + spare_bonus(frames, i)
        else:
            score += sum(frames[i])
    return score


def is_strike(frame):
    return frame[0] == N_PINS


def is_spare(frame):
    return sum(frame) == N_PINS


def strike_bonus(frames, i):
    if is_strike(frames[i + 1]):
        return N_PINS + frames[i + 2][0]

    last_ball = 9
    if i == last_ball:
        return sum(flatten(frames[i + 1: i + 3]))
    return sum(frames[i + 1])


def spare_bonus(frames, i):
    return frames[i + 1][0]
