import math

data = open("input.txt", "r")

with open("input.txt", "r") as f:
    content = f.readlines()

    password = 0
    dial = 50

    for line in content:
        direction = line[0]
        num = int(line[1:])
        count = math.floor((num / 100))

        if direction == "R":
            dial += (num % 100)
        else:
            dial -= (num % 100)

        if dial < 0:
            dial += 100
            count += 1
        elif dial > 99:
            dial -= 100
            count += 1
        
        if dial == 0:
            count += 1

        password += count

    print(password)


