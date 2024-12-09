from dataclasses import replace


def part_one():
    with open("input.txt", "r") as file:
        disk_content = file.readline()
    disk_content_with_free_space = []
    id = 0
    steps = 0
    while steps < len(disk_content):
        if steps % 2 == 0:
            for i in range(int(disk_content[steps])):
                disk_content_with_free_space.append(str(id))
            id += 1
        else:
            for i in range(int(disk_content[steps])):
                disk_content_with_free_space.append(".")
        steps += 1

    print(disk_content_with_free_space)
    result = list(disk_content_with_free_space)
    start = 0
    end = -1
    while start != len(result) + end and start < len(result):
        if result[start] == ".":
            if result[end] != ".":
                result[start], result[end] = result[end], result[start]
            else:
                end -= 1
        else:
            if result[end] == ".":
                end -= 1
            else:
                start += 1

    print(f"result is {"".join(result)}")

    id = 0
    checksum = 0
    while id < len(result) and result[id] != ".":
        checksum += id * int(result[id])
        id += 1
    print(f"checksum is {checksum}")


def part_two():
    with open("input.txt", "r") as file:
        disk_content = file.readline()
    disk_content_with_free_space = []
    id = 0
    steps = 0
    while steps < len(disk_content):
        if steps % 2 == 0:
            for i in range(int(disk_content[steps])):
                disk_content_with_free_space.append(str(id))
            id += 1
        else:
            for i in range(int(disk_content[steps])):
                disk_content_with_free_space.append(".")
        steps += 1

    disk_content_with_free_space_list = list(disk_content_with_free_space)
    i = 0
    result = disk_content_with_free_space_list.copy()
    files_length_by_id = {}

    for item in disk_content_with_free_space_list:
        if item != "." and item.isdigit():
            id = int(item)
            if id in files_length_by_id:
                files_length_by_id[id] += 1
            else:
                files_length_by_id[id] = 1

    print(files_length_by_id)
    replaced_indices = []
    print(len(disk_content_with_free_space_list))
    last_number = 0
    while i < len(disk_content_with_free_space_list) and len(files_length_by_id) > 0:
        if i not in replaced_indices and disk_content_with_free_space_list[i] == ".":
            free_space_length = 1
            while i + free_space_length < len(disk_content_with_free_space_list) and disk_content_with_free_space_list[i + free_space_length] == "." and (i + free_space_length) not in replaced_indices:
                free_space_length += 1

            candidates = [id for id, value in files_length_by_id.items() if value <= free_space_length]

            if candidates:
                best_candidate = max(candidates)
                if best_candidate < last_number:
                    i += 1
                    continue
                tmp = [i for i, x in enumerate(result) if x == str(best_candidate)]
                result = ["." if i in tmp else x for i, x in enumerate(result)]
                result = ["." if x == str(best_candidate) else x for x in result]
                replaced_indices.extend(tmp)
                for j in range(files_length_by_id[best_candidate]):
                    result[i + j] = str(best_candidate)
                i += files_length_by_id[best_candidate]
                del files_length_by_id[best_candidate]
            else:
                i += 1

        else:
            if disk_content_with_free_space_list[i] != ".":
                last_number = int(disk_content_with_free_space_list[i])
            i += 1
        print(i)

    print(f"final_result: {result}")

    id = 0
    checksum = 0
    while id < len(result):
        if result[id] == ".":
            id += 1
        else:
            checksum += id * int(result[id])
            id += 1
    print(f"checksum is {checksum}")


if __name__=="__main__":
    # part_one()
    part_two()
