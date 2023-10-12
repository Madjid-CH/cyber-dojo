import pytest

from harry_poter.main import *


def example():
    input_ = (
        "2 copies of the first book\n"
        "2 copies of the second book\n"
        "2 copies of the third book\n"
        "1 copy of the fourth book\n"
        "1 copy of the fifth book\n"
    )
    cost = 51.20
    return input_, cost


def test_parse():
    input_, _ = example()
    assert parse(input_) == [2, 2, 2, 1, 1]


def test_no_discount():
    books = [1, 1, 2, 2, 3]
    price = sum(books * BOOK_COST)
    assert calculate_price(books, discount=0.0) == price


def test_discount():
    books = [1, 1, 2, 2, 3]
    price = sum(books * BOOK_COST) * 0.95
    assert calculate_price(books, discount=0.05) == price


def test_is_no_discount_applicable():
    books = [1, 1, 2, 2, 3]
    assert is_discount_applicable(books, 0)


@pytest.mark.parametrize(
    "books, expected", [([0, 0, 2, 0, 0], False), ([1, 1, 2, 2, 1], True)]
)
def test_is_5_discount_applicable(books, expected):
    assert is_discount_applicable(books, 0.05) == expected


@pytest.mark.parametrize(
    "books, expected",
    [([0, 0, 2, 1, 0], False), ([1, 1, 2, 0, 0], True), ([1, 1, 2, 2, 1], True)],
)
def test_is_10_discount_applicable(books, expected):
    assert is_discount_applicable(books, 0.1) == expected


@pytest.mark.parametrize(
    "books, expected",
    [([3, 0, 2, 1, 0], False), ([1, 1, 2, 5, 0], True), ([1, 1, 2, 2, 1], True)],
)
def test_is_20_discount_applicable(books, expected):
    assert is_discount_applicable(books, 0.2) == expected


@pytest.mark.parametrize(
    "books, expected",
    [([3, 0, 2, 1, 1], False), ([1, 1, 2, 2, 1], True)],
)
def test_is_25_discount_applicable(books, expected):
    assert is_discount_applicable(books, 0.25) == expected


@pytest.mark.parametrize(
    "books, discount, expected",
    [
        ([1, 1, 2, 2, 1], 0.25, [1, 1, 1, 1, 1]),
        ([1, 1, 2, 2, 1], 0.20, [1, 1, 1, 1, 0]),
        ([0, 1, 2, 2, 1], 0.20, [0, 1, 1, 1, 1]),
        ([1, 1, 2, 2, 1], 0.10, [1, 1, 1, 0, 0]),
        ([3, 1, 2, 2, 1], 0.05, [1, 1, 0, 0, 0]),
        ([0, 1, 2, 2, 1], 0.05, [0, 1, 1, 0, 0]),
        ([0, 0, 2, 2, 1], 0.05, [0, 0, 1, 1, 0]),
    ],
)
def test_get_books_for_discount(books, discount, expected):
    assert get_books_for_discount(books, discount=discount) == expected


@pytest.mark.parametrize(
    "books, expected",
    [([1, 1, 1, 1, 1], [0, 0, 0, 0, 0]), ([1, 1, 2, 2, 1], [0, 0, 1, 1, 0])],
)
def test_applying_25_discount(books, expected):
    price, remaining_books = apply_discount(books, discount=0.25)
    assert price == 5 * BOOK_COST * 0.75
    assert remaining_books == expected


@pytest.mark.parametrize(
    "books, expected",
    [
        ([1, 1, 1, 1, 1], [0, 0, 0, 0, 1]),
        ([0, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
        ([1, 1, 2, 2, 1], [0, 0, 1, 1, 1]),
    ],
)
def test_applying_20_discount(books, expected):
    price, remaining_books = apply_discount(books, discount=0.20)
    assert price == 4 * BOOK_COST * 0.80
    assert remaining_books == expected


@pytest.mark.parametrize(
    "books, expected",
    [
        ([1, 1, 1, 1, 1], [0, 0, 0, 1, 1]),
        ([0, 1, 1, 1, 1], [0, 0, 0, 0, 1]),
        ([1, 1, 2, 2, 1], [0, 0, 1, 2, 1]),
    ],
)
def test_applying_10_discount(books, expected):
    price, remaining_books = apply_discount(books, discount=0.10)
    assert price == 3 * BOOK_COST * 0.90
    assert remaining_books == expected


@pytest.mark.parametrize(
    "books, expected",
    [
        ([1, 1, 1, 1, 1], [0, 0, 1, 1, 1]),
        ([0, 1, 1, 1, 1], [0, 0, 0, 1, 1]),
        ([1, 1, 2, 2, 1], [0, 0, 2, 2, 1]),
    ],
)
def test_applying_5_discount(books, expected):
    price, remaining_books = apply_discount(books, discount=0.05)
    assert price == 2 * BOOK_COST * 0.95
    assert remaining_books == expected


def test_of_acceptance():
    input_, cost = example()
    assert calculate_total_price(parse(input_)) == cost
