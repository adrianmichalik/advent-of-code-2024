def part_one():
    left_numbers = []
    right_numbers = []

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))

    left_numbers.sort()
    right_numbers.sort()
    total_distance = 0
    for i in range(len(left_numbers)):
        total_distance += abs(left_numbers[i] - right_numbers[i])
    print(f"total distance is {total_distance}")


def part_two():
    left_numbers = []
    right_numbers = []

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))

    occurrences_map = {}
    for number in right_numbers:
        if number in occurrences_map:
            occurrences_map[number] += 1
        else:
            occurrences_map[number] = 1

    similarity_score = 0
    for number in left_numbers:
        if number in occurrences_map:
            similarity_score += number * occurrences_map[number]

    print(f"similarity score is {similarity_score}")


# Using the special variable
# __name__
if __name__=="__main__":
    # part_one()
    part_two()
