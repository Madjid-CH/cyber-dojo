from collections import OrderedDict

from more_itertools import sliding_window

CARDS_ORDER = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")


def parse_input(input):
    input = input.split()
    black_hand = input[1:6]
    white_hand = input[7:12]
    return {"Black": black_hand, "White": white_hand}


def straight_flush(black_hand, white_hand):
    black_highest_value = hand_highest_value(black_hand)
    white_highest_value = hand_highest_value(white_hand)
    return decide_winner(black_highest_value, white_highest_value)


def hand_highest_value(hand):
    values = [card[0] for card in hand]
    return max(values)


def count_highest_same_suit(hand):
    suits = [card[-1] for card in hand]
    return max([suits.count(suit) for suit in suits])


def count_consecutive_values_by_suit(hand):
    suits = set([card[1] for card in hand])
    suit_values = {suit: [] for suit in suits}
    for value, suit in hand:
        suit_values[suit].append(value)
    counts = {suit: 0 for suit in suits}
    for suit, values in suit_values.items():
        values = sorted(values, key=CARDS_ORDER.index)
        counts[suit] = match_consecutive_values(values)
    return counts


def match_consecutive_values(values):
    possible_number_of_consecutive_values = [5, 4, 3, 2]
    for n in possible_number_of_consecutive_values:
        sliced_values = sliding_window(values, n)
        sliced_ordered_cards = sliding_window(
            CARDS_ORDER,
            n,
        )
        for sv, soc in zip(sliced_values, sliced_ordered_cards):
            if list(sv) == list(soc):
                return n
    return 1


def highest_consecutive_value(hand):
    return max(count_consecutive_values_by_suit(hand).values())


def four_of_a_kind(black_hand, white_hand):
    black_fours = get_same_highest_n_cards(black_hand, 4)
    white_fours = get_same_highest_n_cards(white_hand, 4)
    black_value = black_fours[0][0]
    white_value = white_fours[0][0]
    return decide_winner(black_value, white_value)


def get_same_highest_n_cards(hand, n):
    grouped_values = group_cards_by_value(hand)
    sorted_grouped_values = sorted(
        grouped_values.items(),
        key=lambda x: order_of(value_of(x[0])),
        reverse=True,
    )
    for v, cards in sorted_grouped_values:
        if len(cards) == n:
            return cards


def order_of(v):
    return CARDS_ORDER.index(v)


def full_house(black_hand, white_hand):
    black_threes = get_same_highest_n_cards(black_hand, 3)
    white_threes = get_same_highest_n_cards(white_hand, 3)
    black_value = black_threes[0][0]
    white_value = white_threes[0][0]
    return decide_winner(black_value, white_value)


def flush(black_hand, white_hand):
    return high_card(black_hand, white_hand)


def high_card(black_hand, white_hand):
    ordered_black_hand = sorted(
        black_hand, key=lambda card: order_of(value_of(card)), reverse=True
    )
    ordered_white_hand = sorted(
        white_hand, key=lambda card: order_of(value_of(card)), reverse=True
    )
    for black_card, white_card in zip(ordered_black_hand, ordered_white_hand):
        result = decide_winner(value_of(black_card), value_of(white_card))
        if result[0] != "Tie":
            return result

    return result


def value_of(card):
    return card[0]


def suit_of(card):
    return card[1]


def hand_highest_card(hand):
    return max(hand, key=lambda x: order_of(x[0]))


def straight(black_hand, white_hand):
    return high_card(black_hand, white_hand)


def three_of_a_kind(black_hand, white_hand):
    black_threes = get_same_highest_n_cards(black_hand, 3)
    white_threes = get_same_highest_n_cards(white_hand, 3)
    black_value = black_threes[0][0]
    white_value = white_threes[0][0]
    return decide_winner(black_value, white_value)


def decide_winner(black_value, white_value):
    if order_of(black_value) > order_of(white_value):
        return "Black", black_value
    elif order_of(black_value) < order_of(white_value):
        return "White", white_value
    else:
        return "Tie", black_value


def two_pairs(black_hand, white_hand):
    black_grouped_cards = group_cards_by_value(black_hand)
    white_grouped_cards = group_cards_by_value(white_hand)
    black_highest_pair, black_lowest_pair = get_two_pairs(black_grouped_cards)
    white_highest_pair, white_lowest_pair = get_two_pairs(white_grouped_cards)
    result = decide_winner(
        value_of(black_highest_pair[0]), value_of(white_highest_pair[0])
    )
    if result[0] != "Tie":
        return result

    result = decide_winner(
        value_of(black_lowest_pair[0]), value_of(white_lowest_pair[0])
    )
    if result[0] != "Tie":
        return result

    (last_white_card,) = get_remaining_card(white_grouped_cards)
    (last_black_card,) = get_remaining_card(black_grouped_cards)
    return decide_winner(value_of(last_black_card), value_of(last_white_card))


def get_remaining_card(grouped_cards):
    last_cards = []
    for v, cards in grouped_cards.items():
        if len(cards) == 1:
            last_cards.append(cards[0])
    return last_cards


def get_two_pairs(grouped_cards):
    pairs = []
    sorted_groups = sorted(
        grouped_cards.items(), key=lambda x: order_of(value_of(x[0])), reverse=True
    )
    for v, cards in sorted_groups:
        if len(cards) == 2:
            pairs.append(cards)
    return pairs[0], pairs[1]


def group_cards_by_value(hand):
    values = set([value_of(card) for card in hand])
    grouped_cards = {v: [] for v in values}
    for card in hand:
        grouped_cards[value_of(card)].append(card)
    return grouped_cards


def pair(black_hand, white_hand):
    black_pair = get_same_highest_n_cards(black_hand, 2)
    white_pair = get_same_highest_n_cards(white_hand, 2)
    result = decide_winner(value_of(black_pair[0]), value_of(white_pair[0]))
    if result[0] != "Tie":
        return result

    remaining_black_cards = get_remaining_card(group_cards_by_value(black_hand))
    remaining_white_cards = get_remaining_card(group_cards_by_value(white_hand))
    return high_card(remaining_black_cards, remaining_white_cards)


def hand_category(hand):
    if count_highest_same_suit(hand) == 5:
        counts = count_consecutive_values_by_suit(hand)
        if max(counts.values()) == 5:
            return "straight flush"

    if get_same_highest_n_cards(hand, 4):
        return "four of a kind"

    if get_same_highest_n_cards(hand, 3):
        if get_same_highest_n_cards(hand, 2):
            return "full house"
        return "three of a kind"

    if count_highest_same_suit(hand) == 5:
        counts = count_consecutive_values_by_suit(hand)
        if max(counts.values()) != 5:
            return "flush"

    if count_highest_same_suit(hand) != 5:
        values = [value_of(card) for card in hand]
        if match_consecutive_values(values) == 5:
            return "straight"
    hand_copy = hand.copy()
    if pair := get_same_highest_n_cards(hand, 2):
        for c in pair:
            hand_copy.remove(c)
        if get_same_highest_n_cards(hand_copy, 2):
            return "two pairs"
        return "pair"

    return "high card"


def scorers():
    category_scorers = OrderedDict()
    category_scorers["straight flush"] = straight_flush
    category_scorers["four of a kind"] = four_of_a_kind
    category_scorers["full house"] = full_house
    category_scorers["flush"] = flush
    category_scorers["straight"] = straight
    category_scorers["three of a kind"] = three_of_a_kind
    category_scorers["two pairs"] = two_pairs
    category_scorers["pair"] = pair
    category_scorers["high card"] = high_card
    return category_scorers


category_scorers = scorers()


def poker(input):
    hands = parse_input(input)
    black_hand = hands["Black"]
    white_hand = hands["White"]
    black_category = hand_category(black_hand)
    white_category = hand_category(white_hand)
    if black_category == white_category:
        return handle_same_category(black_hand, white_hand, black_category)
    else:
        pass
    return handle_different_category(black_category, white_category)


def handle_same_category(black_hand, white_hand, category):
    scorer = category_scorers[category]
    score = scorer(black_hand, white_hand)
    result = score[0]
    if result == "Tie":
        return result
    winning_card = score[1] if score[1] != "A" else "Ace"
    return f"{result} wins - {category}: {winning_card}"


def handle_different_category(black_category, white_category):
    category_order = tuple(category_scorers.keys())
    black_category_order = category_order.index(black_category)
    white_category_order = category_order.index(white_category)
    if black_category_order < white_category_order:
        return f"Black wins - {black_category}"
    else:
        return f"White wins - {white_category}"
