from itertools import chain, combinations, permutations, product


class Operation:
    def __init__(self, result, components):
        self.result = result
        self.components = components
        self.combinations = []
        self.valid = False

    def __repr__(self):
        return f"Operation(result={self.result}, components={self.components})"


def parse_input():
    operations = []
    with open("input.txt", "r") as file:
        for line in file:
            if line.strip():
                result, *components = line.replace(":", "").split()
                result = int(result)
                components = list(map(int, components))
                operations.append(Operation(result, components))
    return operations


def part_one():
    operations = parse_input()
    operators = ("+", "*")
    for operation in operations:
        all_operators = list(product(operators, repeat=len(operation.components) - 1))
        for op in all_operators:
            result = operation.components[0]
            for index, number in enumerate(operation.components):
                if index > 0:
                    if op[index - 1] == '+':
                        result += number
                    else:
                        result *= number
            if result == operation.result:
                operation.valid = True
    valid_operations_result = 0
    for operation in operations:
        if operation.valid:
            valid_operations_result += operation.result
    print(f"valid operations result is {valid_operations_result}")


def part_two():
    operations = parse_input()
    operators = ("+", "*", "||")
    for operation in operations:
        all_operators = list(product(operators, repeat=len(operation.components) - 1))
        for op in all_operators:
            result = operation.components[0]
            for index, number in enumerate(operation.components):
                if index > 0:
                    if op[index - 1] == '+':
                        result += number
                    elif op[index - 1] == '||':
                        result = int(str(result) + str(number))
                    else:
                        result *= number
            if result == operation.result:
                operation.valid = True
    valid_operations_result = 0
    for operation in operations:
        if operation.valid:
            valid_operations_result += operation.result
    print(f"valid operations result is {valid_operations_result}")


if __name__=="__main__":
    part_one()
    part_two()
