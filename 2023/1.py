f = open("input.txt", "r")
line = f.readline()
linesum = 0
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
while line:
    d1 = ""
    for i in range(len(line)):
        for d in digits.keys():
            if d in line[:i]:
                d1 = digits[d]
        if not d1 and line[i].isdigit():
            d1 = line[i]
        if d1:
            break
    d2 = ""
    for i in reversed(range(len(line))):
        for d in digits.keys():
            if d in line[i:]:
                d2 = digits[d]
        if not d2 and line[i].isdigit():
            d2 = line[i]
        if d2:
            break
    linesum += int(d1 + d2)
    line = f.readline()

print(linesum)
