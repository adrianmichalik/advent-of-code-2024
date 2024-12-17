import re
from sympy import symbols, Eq, solve


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class InputData:
    def __init__(self, button_a: Point, button_b: Point, prize: Point):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __repr__(self):
        return f"InputData(Button A: {self.button_a}, Button B: {self.button_b}, Prize: {self.prize})"


def parse_input_file():
    button_pattern = re.compile(r"Button (A|B): X\+([0-9]+), Y\+([0-9]+)")
    prize_pattern = re.compile(r"Prize: X=([0-9]+), Y=([0-9]+)")

    with open('input.txt', 'r') as file:
        lines = file.read().strip().split('\n\n')

    results = []
    for block in lines:
        button_a, button_b, prize = None, None, None
        for line in block.split('\n'):
            button_match = button_pattern.match(line)
            if button_match:
                button = Point(int(button_match.group(2)), int(button_match.group(3)))
                if button_match.group(1) == 'A':
                    button_a = button
                elif button_match.group(1) == 'B':
                    button_b = button

            prize_match = prize_pattern.match(line)
            if prize_match:
                prize = Point(int(prize_match.group(1)), int(prize_match.group(2)))

        results.append(InputData(button_a, button_b, prize))

    return results


def parse_input_file_pt2():
    button_pattern = re.compile(r"Button (A|B): X\+([0-9]+), Y\+([0-9]+)")
    prize_pattern = re.compile(r"Prize: X=([0-9]+), Y=([0-9]+)")

    with open('input.txt', 'r') as file:
        lines = file.read().strip().split('\n\n')

    results = []
    for block in lines:
        button_a, button_b, prize = None, None, None
        for line in block.split('\n'):
            button_match = button_pattern.match(line)
            if button_match:
                button = Point(int(button_match.group(2)), int(button_match.group(3)))
                if button_match.group(1) == 'A':
                    button_a = button
                elif button_match.group(1) == 'B':
                    button_b = button

            prize_match = prize_pattern.match(line)
            if prize_match:
                prize = Point(int(prize_match.group(1)) + 10000000000000, int(prize_match.group(2)) + 10000000000000)

        results.append(InputData(button_a, button_b, prize))

    return results


def solve_equations(a1, b1, c1, a2, b2, c2):
    n, m = symbols('n m')

    eq1 = Eq(a1 * n + b1 * m, c1)
    eq2 = Eq(a2 * n + b2 * m, c2)

    solution = solve((eq1, eq2), (n, m))

    if solution:
        n_value = solution[n]
        m_value = solution[m]
        print(f"Solved: n = {n_value}, m = {m_value}")

        if n_value.is_integer and m_value.is_integer:
            return n_value, m_value
        else:
            return None
    else:
        return None


def part_one():
    data = parse_input_file()

    tokens_total = 0
    for entry in data:
        print(entry)
        number_of_tokens = 100000000000000
        for i in range(100, 0, -1):
            # przypadek 1 - lepiej wiecej razy wcisnac A
            remaining_prize_x = entry.prize.x - (i * entry.button_a.x)
            if remaining_prize_x > 0:
                remaining_prize_y = entry.prize.y - (i * entry.button_a.y)
                if remaining_prize_y > 0:
                    number_of_b_clicks_x = remaining_prize_x / entry.button_b.x
                    number_of_b_clicks_y = remaining_prize_y / entry.button_b.y
                    if number_of_b_clicks_x == number_of_b_clicks_y:
                        number_of_tokens_candidate = (3 * i) + (1 * number_of_b_clicks_x)
                        if number_of_tokens_candidate < number_of_tokens:
                            number_of_tokens = number_of_tokens_candidate
                    else:
                        continue
                else:
                    continue
            else:
                continue
        if number_of_tokens < 100000000000000:
            tokens_total += number_of_tokens
    print(tokens_total)


def part_two():
    data = parse_input_file_pt2()

    tokens_total = 0
    for entry in data:
        result = solve_equations(entry.button_a.x, entry.button_b.x, entry.prize.x, entry.button_a.y, entry.button_b.y, entry.prize.y)
        if result is not None:
            tokens_total += 3 * result[0] + result[1]
    print(tokens_total)


if __name__ == "__main__":
    # part_one()
    part_two()
