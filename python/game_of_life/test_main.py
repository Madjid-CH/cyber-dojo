import pytest
from game_of_life.main import (
    step,
    count_neighbours,
    get_neighbours,
    off_boundary,
    parse,
)


def one_cell():
    return [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def empty_world():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_empty_world():
    assert step(empty_world()) == empty_world()


def test_single_cell():
    assert step(one_cell()) == empty_world()


def two_cells():
    return [[0, 0, 0], [0, 1, 1], [0, 0, 0]]


def test_two_cells():
    world = two_cells()
    assert step(world) == empty_world()


def test_overcrowding():
    world = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    assert step(world) == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]


def stable_world():
    return [[1, 1, 0], [1, 1, 0], [0, 0, 0]]


def test_stable_world():
    world = stable_world()
    assert step(world) == world


def test_new_cells():
    world = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
    assert step(world) == stable_world()


@pytest.mark.parametrize(
    "world, count",
    [
        (empty_world(), 0),
        (one_cell(), 0),
        (two_cells(), 1),
        ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 4),
    ],
)
def test_count_neighbours(world, count):
    assert count_neighbours(world, (1, 1)) == count


def test_get_neighbours():
    world = two_cells()
    assert get_neighbours(world, (1, 1)) == [0, 0, 0, 0, 1, 0, 0, 0]


@pytest.mark.parametrize(
    "world, cell, neighbours",
    [
        (empty_world(), (0, 0), [0, 0, 0, 0, 0, 0, 0, 0]),
        (one_cell(), (1, 1), [0, 0, 0, 0, 0, 0, 0, 0]),
        (two_cells(), (1, 0), [0, 0, 0, 0, 1, 0, 0, 0]),
    ],
)
def test_get_border_cell_neighbours(world, cell, neighbours):
    assert get_neighbours(world, cell) == neighbours


def test_off_boundary():
    assert off_boundary(empty_world(), 1, 3) == True


def example1():
    input_ = "........\n....*...\n...**...\n.....*..\n"
    output = "........\n...**...\n...***..\n....*..."
    return input_, output


def example2():
    input_ = "........\n...**...\n.*****..\n........\n........\n"
    output = "........\n.....*..\n..*..*..\n..***...\n........"
    return input_, output


def test_parse():
    world, _ = example2()
    assert parse(world) == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]


def test_example1():
    input_, output = example1()
    assert step(parse(input_)) == parse(output)


def test_example2():
    input_, output = example2()
    assert step(parse(input_)) == parse(output)
