from itertools import combinations, permutations


class Frequency:
    def __init__(self, symbol):
        self.symbol = symbol
        self.locations = []
        self.antinodes = set()

    def __repr__(self):
        return f"Frequency(symbol='{self.symbol}', locations={self.locations}, antinodes={self.antinodes})"


def parse_grid():
    frequencies = {}

    with open('input.txt', 'r') as file:
        grid = file.readlines()

    for y, line in enumerate(grid):
        for x, char in enumerate(line.strip()):
            if char != '.':
                if char not in frequencies:
                    frequencies[char] = Frequency(char)
                frequencies[char].locations.append((x, y))
    rows = len(grid)
    cols = len(grid[0]) - 1

    return rows, cols, frequencies


def reflect_point(center, point):
    center_x, center_y = center
    point_x, point_y = point

    reflected_x = 2 * center_x - point_x
    reflected_y = 2 * center_y - point_y

    return reflected_x, reflected_y


def reflect_multiple_points(center, point, x_limit, y_limit):
    reflected_points = []
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    current_point = point

    while True:
        new_x = current_point[0] + dx
        new_y = current_point[1] + dy

        if not (0 <= new_x < x_limit and 0 <= new_y < y_limit):
            break

        reflected_points.append((new_x, new_y))
        current_point = (new_x, new_y)

    return reflected_points


def calculate_antinodes(frequency: Frequency, rows: int, cols: int):
    location_pairs = list(permutations(frequency.locations, r=2))
    for pair in location_pairs:
        antinode_candidate = reflect_point(pair[0], pair[1])
        if 0 <= antinode_candidate[0] < rows and 0 <= antinode_candidate[1] < cols:
            frequency.antinodes.add(antinode_candidate)


def calculate_multiple_antinodes(frequency: Frequency, rows: int, cols: int):
    location_pairs = list(permutations(frequency.locations, r=2))
    for pair in location_pairs:
        frequency.antinodes.update(reflect_multiple_points(pair[0], pair[1], rows, cols))


def part_one():
    rows, cols, frequencies = parse_grid()

    antinodes = set()
    for frequency in frequencies.values():
        calculate_antinodes(frequency, rows, cols)
        antinodes.update(frequency.antinodes)
    print(f"len: {len(antinodes)}, contains: {antinodes}")


def part_two():
    rows, cols, frequencies = parse_grid()
    antinodes = set()
    for frequency in frequencies.values():
        calculate_multiple_antinodes(frequency, rows, cols)
        antinodes.update(frequency.antinodes)
        if len(frequency.locations) > 1:
            antinodes.update(frequency.locations)
    print(f"part two -> len: {len(antinodes)}, contains: {antinodes}")


if __name__=="__main__":
    part_one()
    part_two()
