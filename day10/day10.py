from collections import deque


def load_grid_from_file(filename):
    with open(filename, 'r') as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]
    return grid


def bfs_find_paths(grid):
    rows = len(grid)
    cols = len(grid[0])
    paths = []

    def get_neighbors(x, y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] + 1:
                neighbors.append((nx, ny))
        return neighbors

    start_points = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 0]

    for start in start_points:
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()
            x, y = current

            if grid[x][y] == 9:
                paths.append(path)
                continue

            for neighbor in get_neighbors(x, y):
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

    return paths


def part_one():
    grid = load_grid_from_file("input.txt")
    paths = bfs_find_paths(grid)
    unique_pairs = set()
    for path in paths:
        start = path[0]
        end = path[-1]
        unique_pairs.add((start, end))
    print(len(unique_pairs))



def part_two():
    grid = load_grid_from_file("input.txt")
    paths = bfs_find_paths(grid)
    print(len(paths))


if __name__ == "__main__":
    part_one()
    part_two()
