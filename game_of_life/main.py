from copy import deepcopy


def step(world: list):
    new_world = deepcopy(world)
    for i, row in enumerate(world):
        for j, cell in enumerate(row):
            new_world[i][j] = update_cell(world, i, j)
    return new_world


def update_cell(world, i, j):
    if underpopulation(world, (i, j)) or overcrowding(world, (i, j)):
        return 0
    if reproduction(world, (i, j)):
        return 1
    return world[i][j]


def reproduction(world, cell):
    return count_neighbours(world, cell) == 3


def overcrowding(world, cell):
    return count_neighbours(world, cell) > 3


def underpopulation(world, cell):
    return count_neighbours(world, cell) < 2


def count_neighbours(world, cell):
    neighbours = get_neighbours(world, cell)
    return sum(neighbours)


def get_neighbours(world, cell):
    row, col = cell
    neighbours = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i != row or j != col:
                neighbours.append(get_neighbour(world, i, j))
    return neighbours


def get_neighbour(world, i, j):
    if off_boundary(world, i, j):
        return 0
    else:
        return world[i][j]


def off_boundary(world, i, j):
    if 0 <= i < len(world) and 0 <= j < len(world[0]):
        return False
    return True


def parse(input_: str):
    lines = input_.splitlines()
    lines = [list(line) for line in lines]
    return [parse_line(line) for line in lines]


def parse_line(line):
    return [parse_cell(cell) for cell in line]


def parse_cell(cell):
    if cell == ".":
        return 0
    else:
        return 1
