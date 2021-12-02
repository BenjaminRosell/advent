import math
from itertools import accumulate


def process_instruction(direction, n):
    if direction == "forward":
        return (n, 0)
    elif direction == "up":
        return (0, -n)
    return (0, n)


def load_instructions():
    directions = []
    with open("data.txt", "r") as file:
        for row in file:
            direction, n = row.split()
            directions.append(process_instruction(direction, int(n)))
    return directions


def process(directions):
    return math.prod(list(map(sum, zip(*directions))))


def process_aim(directions):
    aim_directions = accumulate(list(zip(*directions))[1])
    x_directions = list(zip(*directions))[0]
    return sum([x * y for (x, y) in zip(x_directions, aim_directions)]) * sum(
        x_directions
    )


def main():
    directions = load_instructions()
    print(process(directions))
    print(process_aim(directions))


if __name__ == "__main__":
    main()
