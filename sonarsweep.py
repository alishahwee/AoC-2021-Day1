def part_one(depths: list) -> int:
    num_increases = 0

    for i in range(len(depths)):
        if i == 0:
            continue  #  Skip the first depth
        elif depths[i] > depths[i - 1]:
            num_increases += 1

    return num_increases


def part_two(depths: list) -> int:
    num_increases = 0
    previous_sum = 0
    current_sum = 0

    # Only iterates the possible number of sliding windows
    for i in range(len(depths) - 1):
        if i == 0:  # Skip the first depth
            continue

        previous_sum = current_sum
        current_sum = depths[i - 1] + depths[i] + depths[i + 1]

        if previous_sum != 0 and current_sum > previous_sum:
            num_increases += 1

    return num_increases
