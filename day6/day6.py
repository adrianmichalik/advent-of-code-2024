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


def simulate_grid_with_fake_obstacles(original_grid):
    # probuje w kazdym kolejnym punkcie ustawic przeszkode i zobaczyc czy kiedys guard wyjdzie
    guard_did_not_leave_map = 0
    for i in range(len(original_grid) - 1):
        for j in range(len(original_grid[0])):
            x, y, direction = find_guard(original_grid)
            if i == x and j == y:
                continue
            tmp_grid = copy.deepcopy(original_grid)
            tmp_grid[j][i] = "#"
            guard = Guard(x, y, direction)
            guard_in_the_grid = True
            steps = 0
            max_steps = 10000
            while guard_in_the_grid and steps < max_steps:
                steps += 1
                guard_in_the_grid = guard.move(tmp_grid)
            if guard_in_the_grid:
                print("guard stayed in map")
                guard_did_not_leave_map += 1
    print(f"guard did not leave map count: {guard_did_not_leave_map}")


def part_two(original_grid):
    simulate_grid_with_fake_obstacles(original_grid)


def load_grid():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


if __name__=="__main__":
    guards_path = part_one()
    part_two(load_grid())
