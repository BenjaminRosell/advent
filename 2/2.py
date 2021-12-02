def process_instruction(direction, n):
    if direction == 'forward':
        return (n, 0)
    elif direction == 'up':
        return (0, -n)
    return (0, n)


def load_instructions():
    directions = []
    with open('data.txt', 'r') as file:
        for row in file:
            direction, n = row.split()
            directions.append(process_instruction(direction, int(n)))
    return directions


def process(directions):
    state = list(map(sum, zip(*directions)))
    return state[0] * state[1]


def calculate_depth_position(directions, aim):
    prod = 0
    for i, direction in enumerate(directions):
        prod += direction[0] * aim[i]
    return prod


def process_aim(directions):
    aim = get_aim(list(zip(*directions))[1])
    return calculate_depth_position(directions, aim) * sum(list(zip(*directions))[0])


def get_aim(aim_directions):
    return [sum(aim_directions[:i + 1]) for i, j in enumerate(aim_directions)]


def main():
    directions = load_instructions()
    print(process(directions))
    print(process_aim(directions))


if __name__ == "__main__":
    main()
