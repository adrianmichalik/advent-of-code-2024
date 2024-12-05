from itertools import pairwise


def load_data():
    with open('input.txt', 'r') as f:
        content = f.read()
        first_part = content.strip().split("\n\n")[0]
        second_part = content.strip().split("\n\n")[1]

    order_rules = {}
    for line in first_part.splitlines():
        x, y = map(int, line.split("|"))
        if x not in order_rules:
            order_rules[x] = []
        order_rules[x].append(y)

    instructions = {}
    for line in second_part.splitlines():
        instructions[line.strip()] = True

    print(order_rules)
    return order_rules, instructions


def both_parts():
    order_rules, instructions = load_data()
    for instruction in instructions:
        numbers_from_instruction = list(map(int, instruction.split(',')))
        for number, next_number in pairwise(numbers_from_instruction):
            if number not in order_rules.keys():
                instructions[instruction] = False
                break
            if next_number not in order_rules[number]:
                instructions[instruction] = False
                break


    result = 0
    for instruction in instructions:
        if instructions[instruction]:
            numbers_from_instruction = list(map(int, instruction.split(',')))
            result += numbers_from_instruction[len(numbers_from_instruction) // 2]

    print(instructions)
    print(f"result is {result}")

    wrong_instructions = [list(map(int, key.split(','))) for key, value in instructions.items() if not value]

    for wrong_instruction in wrong_instructions:
        while not is_ordered(wrong_instruction, order_rules):
            for i in range(len(wrong_instruction) - 1):
                if wrong_instruction[i] not in order_rules or wrong_instruction[i+1] not in order_rules[wrong_instruction[i]]:
                    wrong_instruction[i], wrong_instruction[i + 1] = wrong_instruction[i + 1], wrong_instruction[i]

    print(wrong_instructions)
    wrong_instructions_result = 0
    for instruction in wrong_instructions:
        print(instruction[len(instruction) // 2])
        wrong_instructions_result += instruction[len(instruction) // 2]
    print(f"wrong instructions result is {wrong_instructions_result}")


def is_ordered(numbers, order_rules):
    for number, next_number in pairwise(numbers):
        if number not in order_rules.keys():
            return False
        if next_number not in order_rules[number]:
            return False
    return True

if __name__=="__main__":
    both_parts()
