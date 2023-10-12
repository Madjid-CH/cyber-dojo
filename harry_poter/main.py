from itertools import permutations

BOOK_COST = 8

DISCOUNTS = {
    0.0: 1,
    0.05: 2,
    0.10: 3,
    0.20: 4,
    0.25: 5,
}


def calculate_total_price(books):
    prices = []
    for discounts_order in permutations(DISCOUNTS.keys()):
        prices.append(apply_discounts(books.copy(), order=discounts_order))
    return min(prices)


def apply_discounts(books, order):
    price = 0
    for discount in order:
        while is_discount_applicable(books, discount):
            p, books = apply_discount(books, discount)
            price += p
    return price


def parse(input_):
    lines = input_.split("\n")
    return [parse_line(line) for line in lines if line]


def parse_line(line):
    return int(line.split()[0])


def calculate_price(books, discount):
    return sum(books) * BOOK_COST * (1 - discount)


def are_different(books, n_distinct):
    count = books.count(0)
    return count < 5 - (n_distinct - 1)


def is_discount_applicable(books, discount):
    return are_different(books, DISCOUNTS[discount])


def get_books_for_discount(books, discount):
    return get_books_for_discount_helper(books, DISCOUNTS[discount])


def get_books_for_discount_helper(books, num_books):
    res = [0, 0, 0, 0, 0]
    counter = 0
    for i, b in enumerate(books):
        if b > 0:
            res[i] = 1
            counter += 1
        if counter == num_books:
            return res


def apply_discount(books, discount):
    books_for_discount = get_books_for_discount(books, discount=discount)
    price = calculate_price(books_for_discount, discount)
    remaining_books = removed_computed_price_books(books, books_for_discount)
    return price, remaining_books


def removed_computed_price_books(books, to_discount):
    return [a - b for a, b in zip(books, to_discount)]
