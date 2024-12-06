import copy


class Guard:
    DIRECTIONS = ["up", "right", "down", "left"]
    DIRECTION_OFFSETS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.visited_positions = set()
        self.visited_positions.add((x, y))
        self.path = list()
        self.path.append((x, y))

    def move(self, grid):
        dx, dy = self.DIRECTION_OFFSETS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        if not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])):
            return False

        if grid[new_y][new_x] == "#":
            self.rotate_right()
        else:
            self.x, self.y = new_x, new_y
            self.visited_positions.add((new_x, new_y))
            self.path.append((new_x, new_y))
        return True

    def rotate_right(self):
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % 4]

    def place_obstacle(self, grid):
        dx, dy = self.DIRECTION_OFFSETS[self.direction]
        obstacle_x = self.x + dx
        obstacle_y = self.y + dy

        if 0 <= obstacle_y < len(grid) and 0 <= obstacle_x < len(grid[0]):
            grid[obstacle_y][obstacle_x] = "#"


def find_guard(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "^":
                return x, y, "up"


def simulate_guard(grid):
    x, y, direction = find_guard(grid)
    guard = Guard(x, y, direction)

    while True:
        if not guard.move(grid):
            break
    print(f"visited positions count: {len(guard.visited_positions)}")
    return guard.path


def part_one():
    grid = load_grid()
    return simulate_guard(grid)


def simulate_grid_with_fake_obstacles(guards_path, original_grid):
    # probuje w kazdym kolejnym punkcie ustawic przeszkode i zobaczyc czy kiedys guard wyjdzie
    cycles = 0
    for i in range(len(guards_path) - 1):
        print("next iteration")
        next_visited_spot_x, next_visited_spot_y = guards_path[i + 1]
        if next_visited_spot_x > len(guards_path[0]) or next_visited_spot_y > len(guards_path):
            continue
        tmp_grid = copy.deepcopy(original_grid)
        tmp_grid[next_visited_spot_y][next_visited_spot_x] = "#"

        steps_max = 100000
        steps_made = 0
        guard_in_the_grid = True
        x, y, direction = find_guard(tmp_grid)
        guard = Guard(x, y, direction)
        while steps_made < steps_max and guard_in_the_grid:
            print(f"steps_made {steps_made}")
            guard_in_the_grid = guard.move(tmp_grid)
            if not guard_in_the_grid:
                continue
            steps_made += 1
        if steps_made == steps_max and guard_in_the_grid:
            print(f"{next_visited_spot_x}, {next_visited_spot_y}")
            cycles += 1
        print(f"number of cycles: {cycles}")


def part_two(guards_path, original_grid):
    simulate_grid_with_fake_obstacles(guards_path, original_grid)


def load_grid():
    with open('example.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


if __name__=="__main__":
    guards_path = part_one()
    part_two(guards_path, load_grid())
