f = open("input.txt", "r")
line = f.readline()
linesum = 0
isp1 = True
while line:
    digits = {"red": 0, "green": 0, "blue": 0}
    col = line.index(":")
    num = int(line[5:col])
    grabs = line[col + 2 : -1].split("; ")
    for grab in grabs:
        for color in grab.split(", "):
            d, c = color.split(" ")
            digits[c] = max(digits[c], int(d))
    if isp1:
        if digits["red"] <= 12 and digits["green"] <= 13 and digits["blue"] <= 14:
            linesum += num
    else:
        vals = list(digits.values())
        linesum += vals[0] * vals[1] * vals[2]
    line = f.readline()

print(linesum)
