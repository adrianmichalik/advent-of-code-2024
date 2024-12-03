import re


def part_one():
    all_mul_instructions = []
    with open('input.txt', 'r') as file:
        for line in file:
            all_mul_instructions.extend(find_all_mul_instructions(line))
    print(all_mul_instructions)
    result = 0
    for instruction in all_mul_instructions:
        result += multiply(instruction)
    print(f"result is {result}")


def find_all_mul_instructions(text) -> list[str]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    print(matches)
    return matches


def multiply(instruction: str) -> int:
    pattern = r"^mul\((\d{1,3}),(\d{1,3})\)$"
    match = re.match(pattern, instruction)
    x = int(match.group(1))
    y = int(match.group(2))
    return x * y


def part_two():
    doable_instructions = []
    text = ""
    with open('input.txt', 'r') as file:
        for line in file:
            text += line
    text = text.replace("\n", "").replace("\r", "")
    print(text)
    doable_instructions.extend(find_all_doable_instructions(text))
    print(doable_instructions)
    result = 0
    for instruction in doable_instructions:
        result += multiply(instruction)
    print(f"doable instructions result is {result}")


def find_all_doable_instructions(text: str) -> list[str]:
    matches = []
    pattern = r"do\([^)]*\)((?:(?!don't\().)*?mul\(\d{1,3},\d{1,3}\))+"
    tmp_matches = re.finditer(pattern, text)
    for match in tmp_matches:
        group = match.group(0)
        matches.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)", group))
    print(matches)
    return matches


if __name__=="__main__":
    part_one()
    part_two()
