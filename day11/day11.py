from collections import Counter
from math import log10, isqrt


def part_one():
    with open("input.txt", "r") as file:
        stones = list(map(int, file.readline().split()))
    stones_count = 0
    for stone in stones:
        tmp = [stone]
        for i in range(25):
            tmp = apply_rules(tmp)
        stones_count += len(tmp)

    print(stones_count)


def apply_rules(stones_array) -> list[int]:
    result = []
    for stone in stones_array:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            left_half = str(stone)[:middle]
            right_half = str(stone)[middle:]
            result.append(int(left_half))
            result.append(int(right_half))
        else:
            result.append(stone * 2024)
    return result


def apply_rules_with_counter(stone_counts):
    new_counts = Counter()

    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] += count
        else:
            length = int(log10(stone)) + 1
            if length % 2 == 0:
                half_length = length // 2
                divisor = 10 ** half_length
                left = stone // divisor
                right = stone % divisor
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_stone = stone * 2024
                new_counts[new_stone] += count

    return new_counts


def part_two():
    with open("input.txt", "r") as file:
        stones = list(map(int, file.readline().split()))

    stone_counts = Counter(stones)

    for _ in range(75):
        stone_counts = apply_rules_with_counter(stone_counts)
        total_stones = sum(stone_counts.values())

    print(total_stones)


if __name__ == "__main__":
    part_one()
    part_two()
