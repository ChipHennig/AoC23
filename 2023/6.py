f = open("input.txt", "r")
line = f.readline()
col = line.index(":") + 1
time = int(line[col:-1].replace(" ", ""))
line = f.readline()
col = line.index(":") + 1
dist = int(line[col:-1].replace(" ", ""))
ways = 0

for t in range(1, time):
    if (t * (time - t)) > dist:
        ways += 1

print(ways)
