import re

import aocd


data = aocd.get_data(day=1, year=2023).split("\n")
num_list = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"
}


def get_line_sequence(line, pattern):
    matches = re.findall(pattern, line)
    first = matches[0] if matches[0].isdigit() else num_list[matches[0]]
    last = matches[-1] if matches[-1].isdigit() else num_list[matches[-1]]
    return int(first + last)


def part1():
    pattern = r"(\d)"
    nums = [get_line_sequence(line, pattern) for line in data]
    print(sum(nums))


def part2():
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))'
    nums = [get_line_sequence(line, pattern) for line in data]
    print(sum(nums))


if __name__ == "__main__":
    part1()
    part2()