def part_one():
    with open('input.txt', 'r') as file:
        reports = [list(map(int, line.split())) for line in file]

    safe_reports_count = 0
    for report in reports:
        if _is_report_safe(report):
            safe_reports_count += 1

    print(f"safe reports count is {safe_reports_count}")


def part_two():
    with open('input.txt', 'r') as file:
        reports = [list(map(int, line.split())) for line in file]

    result = {"safe": [], "unsafe": []}

    for report in reports:
        if _is_report_safe(report):
            result["safe"].append(report)
        else:
            result["unsafe"].append(report)

    fixable_reports_count = 0
    for unsafe_report in result['unsafe']:
        if _can_be_tolerated(unsafe_report):
            fixable_reports_count += 1

    print(f"Safe reports count: {len(result['safe'])}")
    print(f"Fixable reports count: {fixable_reports_count}")


def _is_report_safe(report) -> bool:
    return (_is_increasing(report) or _is_decreasing(report)) and _is_difference_enough(report)


def _is_increasing(report):
    return all(report[i] < report[i + 1] for i in range(len(report) - 1))


def _is_decreasing(report):
    return all(report[i] > report[i + 1] for i in range(len(report) - 1))


def _is_difference_enough(report):
    return all(abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def _can_be_tolerated(report: list[int]) -> bool:
    for i in range(len(report)):
        if _is_report_safe(report[:i] + report[i+1:]):
            return True
    return False

if __name__=="__main__":
    part_one()
    part_two()