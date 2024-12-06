class Guard:
    DIRECTIONS = ["up", "right", "down", "left"]  # Kierunki w kolejności zgodnej z ruchem wskazówek zegara
    DIRECTION_OFFSETS = {
        "up": (0, -1),   # Ruch w górę: zmiana y o -1
        "down": (0, 1),  # Ruch w dół: zmiana y o +1
        "left": (-1, 0), # Ruch w lewo: zmiana x o -1
        "right": (1, 0)  # Ruch w prawo: zmiana x o +1
    }

    def __init__(self, x, y, direction):
        """
        Initialize the Guard with a position and direction.
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.visited_positions = set()  # Zbiór odwiedzonych pól
        self.visited_positions.add((x, y))  # Dodaj początkową pozycję
        self.cycles = 0  # Licznik cykli

    @property
    def position(self):
        """Return the current position of the guard as a tuple (x, y)."""
        return self.x, self.y

    def move(self, grid):
        """
        Move the guard in the current direction. If it encounters a #, rotate 90 degrees right.
        """
        dx, dy = self.DIRECTION_OFFSETS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        # Check grid boundaries
        if not (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0])):
            return False  # Guard has left the grid

        if grid[new_y][new_x] == "#":
            self.rotate_right()
        else:
            self.x, self.y = new_x, new_y
            if (new_x, new_y) in self.visited_positions:
                self.cycles += 1  # Increment cycle count if revisiting
            else:
                self.visited_positions.add((new_x, new_y))
        return True

    def rotate_right(self):
        """Rotate the guard 90 degrees to the right."""
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % 4]

    def place_obstacle(self, grid):
        """
        Place a temporary # in front of the guard's current direction.
        """
        dx, dy = self.DIRECTION_OFFSETS[self.direction]
        obstacle_x = self.x + dx
        obstacle_y = self.y + dy

        if 0 <= obstacle_y < len(grid) and 0 <= obstacle_x < len(grid[0]):
            grid[obstacle_y][obstacle_x] = "#"

    def __str__(self):
        """Return a string representation of the guard."""
        return (f"Guard position: ({self.x}, {self.y}), facing: {self.direction}, "
                f"unique fields visited: {len(self.visited_positions)}, cycles: {self.cycles}")


def simulate_guard_with_obstacles(grid):
    """
    Simulate the guard's movement with obstacles added before each step.
    """
    x, y, direction = find_guard(grid)
    guard = Guard(x, y, direction)

    print("Simulation started.")
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 10  # Arbitrary large limit to prevent infinite loops

    while True:
        if steps > max_steps:
            print("Simulation terminated due to too many steps (possible infinite loop).")
            break

        print(guard)
        guard.place_obstacle(grid)  # Place an obstacle before moving
        if not guard.move(grid):
            print("Guard has left the grid!")
            break

        steps += 1

    print(f"Total unique fields visited: {len(guard.visited_positions)}")
    print(f"Total cycles detected: {guard.cycles}")


def find_guard(grid):
    """
    Find the initial position and direction of the guard in the grid.
    """
    direction_symbols = {"^": "up", "v": "down", "<": "left", ">": "right"}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in direction_symbols:
                return x, y, direction_symbols[cell]
    raise ValueError("No guard found in the grid.")


def load_grid(filename="example.txt"):
    """
    Load the grid from a file.
    """
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


# Example usage
if __name__ == "__main__":
    grid = load_grid("example.txt")
    simulate_guard_with_obstacles(grid)
