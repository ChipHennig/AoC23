f = open("input.txt", "r")
line = f.readline()
lines = []
while line:
    lines.append(line)
    line = f.readline()

total = 0
copies = [0 for i in range(len(lines))]
for idx, line in enumerate(lines):
    col = line.index(":") + 2
    wins, draws = line[col:-1].split(" | ")
    wins = wins.split()
    draws = draws.split()
    score = 0
    for draw in draws:
        if draw in wins:
            score += 1

    for i in range(idx + 1, idx + 1 + score):
        num_copies = 1
        if copies[idx] != 0:
            num_copies += copies[idx]
        copies[i] += num_copies
    copies[idx] += 1

print(sum(copies))
