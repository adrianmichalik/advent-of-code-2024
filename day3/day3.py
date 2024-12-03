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
    full_text = ""
    with open('input.txt', 'r') as file:
        for line in file:
            full_text += line
    sanitized_text = sanitize_text(full_text)
    text_with_mul_instructions = get_rid_of_not_doable_instructions(sanitized_text)
    all_mul_instructions = find_all_mul_instructions(text_with_mul_instructions)
    result = 0
    for instruction in all_mul_instructions:
        result += multiply(instruction)
    print(f"doable instructions result is {result}")


def sanitize_text(text) -> str:
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)
    cleaned_text = ''.join(matches)
    return cleaned_text


def get_rid_of_not_doable_instructions(text) -> str:
    pattern = r"don't\(\).*?do\(\)"
    cleaned_text = re.sub(pattern, '', text)
    pattern2 = r"don't\(\).*?$"
    cleaned_text = re.sub(pattern2, '', cleaned_text, flags=re.MULTILINE)
    pattern3 = r"do\(\)"
    cleaned_text = re.sub(pattern3, '', cleaned_text)
    return cleaned_text


if __name__=="__main__":
    part_one()
    part_two()
