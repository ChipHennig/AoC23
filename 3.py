import re

f = open("input.txt", "r")
line = f.readline()
mat = []
while line:
    mat.append(line[:-1])
    line = f.readline()


def full_len(ls):
    return sum(map(len, ls))


gears = [[(0, 1) for i in range(len(mat))] for i in range(len(mat))]


def is_part(row, start, end, s):
    lx, ly = len(mat[0]), len(mat)

    for i in range(row - 1, row + 2):
        if i >= 0 and i < ly:
            for j in range(start - 1, end + 2):
                if j >= 0 and j < lx:
                    if mat[i][j] == "*":
                        gears[i][j] = (gears[i][j][0] + 1, gears[i][j][1] * int(s))


linesum = 0
for i, row in enumerate(mat):
    seqs = list(filter(None, re.split(r"(\d+)", row)))
    for idx, s in enumerate(seqs):
        if s.isdigit():
            pos = full_len(seqs[:idx])
            if is_part(i, pos, pos + len(s) - 1, s):
                linesum += int(s)

flat_list = [item for sublist in gears for item in sublist]
gear_ls = list(map(lambda x: x[1], list(filter(lambda x: x[0] == 2, flat_list))))
print(sum(gear_ls))
