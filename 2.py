f = open("input.txt", "r")
line = f.readline()
linesum = 0
while line:
    digits = {"red": 0, "green": 0, "blue": 0}
    col = line.index(":")
    num = int(line[5:col])
    grabs = line[col + 2 : -1].split("; ")
    for grab in grabs:
        for color in grab.split(", "):
            d, c = color.split(" ")
            digits[c] = max(digits[c], int(d))
    vals = list(digits.values())
    linesum += vals[0] * vals[1] * vals[2]
    line = f.readline()

print(linesum)
