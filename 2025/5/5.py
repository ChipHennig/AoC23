data = open("input.txt", "r")

def sol1():
    with open("input.txt", "r") as f:
        content = f.readlines()
        parse_range = False
        ranges = []
        num_fresh = 0
        for line in content:
            if not parse_range:
                if line == "\n":
                    parse_range = True
                else:
                    min_r, max_r = line.split("-")
                    ranges.append((int(min_r), int(max_r)))
            else:
                id_num = int(line)
                for ran in ranges:
                    if id_num >= ran[0] and id_num <= ran[1]:
                        num_fresh += 1
                        break
        print(num_fresh)

def sol2():
    with open("input.txt", "r") as f:
        parse_range = False
        ranges = []
        num_fresh = 0
        while not parse_range:
            line = f.readline()
            if line == "\n":
                parse_range = True
            else:
                min_r, max_r = line.split("-")
                min_r = int(min_r)
                max_r = int(max_r)
                contained = False
                sub_range = 0
                for ran in ranges:
                    if min_r < ran[0] and max_r > ran[1]:
                        sub_range = (ran[1] - ran[0] + 1)
                    if min_r >= ran[0] and max_r <= ran[1]:
                        contained = True
                    elif min_r < ran[0] and max_r >= ran[0] and max_r <= ran[1]:
                        max_r = ran[0] - 1
                    elif min_r >= ran[0] and min_r <= ran[1] and max_r > ran[1]:
                        min_r = ran[1] + 1
                if not contained:
                    ranges.append((min_r, max_r))
                    num_fresh += (max_r - min_r + 1 - sub_range)
        print(num_fresh)

sol2()