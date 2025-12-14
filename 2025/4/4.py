import math

data = open("input.txt", "r")

def sol1():
    with open("input.txt", "r") as f:
        content = f.readlines()

        grid = []

        for line in content:
            grid.append(list(line.rstrip()))

        accessible = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    num_rolls = 0
                    directions = [-1, 0, 1]
                    for xd in directions:
                        for yd in directions:
                            xadj = i + xd
                            yadj = j + yd
                            if not (xd == 0 and yd == 0):
                                if xadj >= 0 and xadj < len(grid) and \
                                    yadj >= 0 and yadj < len(grid[i]):
                                    if grid[xadj][yadj] == "@":
                                        num_rolls += 1
                    if num_rolls < 4:
                        accessible += 1
        
        print(accessible)

def sol2():
    with open("input.txt", "r") as f:
        content = f.readlines()

        grid = []

        for line in content:
            grid.append(list(line.rstrip()))

        removed = 0
        no_removed = False

        while not no_removed:
            sub_removed = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "@":
                        num_rolls = 0
                        directions = [-1, 0, 1]
                        for xd in directions:
                            for yd in directions:
                                xadj = i + xd
                                yadj = j + yd
                                if not (xd == 0 and yd == 0):
                                    if xadj >= 0 and xadj < len(grid) and \
                                        yadj >= 0 and yadj < len(grid[i]):
                                        if grid[xadj][yadj] == "@":
                                            num_rolls += 1
                        if num_rolls < 4:
                            grid[i][j] = "."
                            sub_removed += 1
                            removed += 1
            if sub_removed == 0:
                no_removed = True
        
        print(removed)
            
sol2()