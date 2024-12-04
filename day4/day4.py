def part_one():
    grid = load_grid()
    result = search_word(grid, "XMAS")
    print(f"number of found words is {result}")
    return None


def load_grid():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid


# modified https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
def search_2d(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    if grid[row][col] != word[0]:
        return 0

    len_word = len(word)

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    count = 0

    for direction in range(8):
        curr_x, curr_y = row + x[direction], col + y[direction]
        found_letters = [grid[row][col]]

        while len(found_letters) < len_word:
            if curr_x >= m or curr_x < 0 or curr_y >= n or curr_y < 0:
                break

            if grid[curr_x][curr_y] != word[len(found_letters)]:
                break

            found_letters.append(grid[curr_x][curr_y])

            curr_x += x[direction]
            curr_y += y[direction]

        if len(found_letters) == len_word:
            count += 1

    return count


def search_word(grid, word):
    m = len(grid)
    n = len(grid[0])

    total_count = 0  # Całkowita liczba wystąpień słowa

    for i in range(m):
        for j in range(n):
            total_count += search_2d(grid, i, j, word)

    return total_count


def part_two():
    return None


if __name__=="__main__":
    part_one()
    part_two()
