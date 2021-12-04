from operator import ne, eq, gt, lt, ge


def load_instructions():
    directions = []
    with open("data.txt", "r") as file:
        for row in file:
            directions.append(list(map(int, row[:-1])))
        return directions


def list_to_decimal(binary_list):
    return int("".join(str(x) for x in binary_list), 2)


def compare(column, threshold, relate):
    return list(map(lambda x: 1 if relate(x, int(threshold)) else 0, column))


def process(dirs):
    dir_t = list(zip(*dirs))
    vertical = [sum(dir_t[i]) for i in range(len(dirs[0]))]
    gamma = compare(vertical, len(dirs) / 2, ge)
    epsilon = compare(vertical, len(dirs) / 2, lt)
    return list_to_decimal(gamma) * list_to_decimal(epsilon)


def process_lsr(dirs):
    return oxygen(dirs) * co2(dirs)


def filter_dirs(dirs, remains, relate, i=0):
    while remains > 1:
        dir_t = list(zip(*dirs))
        majority = 1 if sum(dir_t[i]) >= len(dirs) / 2 else 0
        new = []
        [new.append(dirs[idx]) for idx, x in enumerate(dir_t[i]) if relate(x, majority)]
        dirs = new
        remains = len(dirs)
        i += 1
    return dirs[0]


def oxygen(dirs):
    return list_to_decimal(list(filter_dirs(dirs, len(dirs), eq)))


def co2(dirs):
    return list_to_decimal(list(filter_dirs(dirs, len(dirs), ne)))


def main():
    directions = load_instructions()
    print(process(directions))
    print(process_lsr(directions))


if __name__ == "__main__":
    main()
