import math

data = open("input.txt", "r")

def sol1():
    with open("input.txt", "r") as f:
        content = f.read()

        ranges = content.split(",")

        add_ids = 0

        for ran in ranges:
            start, end = ran.split("-")

            print(ran)

            while int(start) < int(end):
                if len(start) % 2 == 0:
                    middle = len(start) // 2
                    first = int(start[:middle])
                    second = int(start[middle:])
                    if first == second:
                        add_ids += int(start)
                        first += 1
                        second = first
                    elif first < second:
                        first += 1
                        second = first
                    else:
                        second = first
                    start = str(first) + str(second)
                else:
                    start = str(10 ** (len(start)))

            if len(end) % 2 == 0:
                middle = len(end) // 2
                first = int(end[:middle])
                second = int(end[middle:])
                if first == second:
                    add_ids += int(start)
                
        
        print(add_ids)

def sol2():
    with open("input.txt", "r") as f:
        content = f.read()

        ranges = content.split(",")

        add_ids = 0

        for ran in ranges:
            start, end = ran.split("-")
            save_digits = 0
            factors = [1]

            while int(start) < int(end):
                digits = len(start)
                found = False
                if digits > 1:
                    if digits != save_digits:
                        factors = [1]
                        for i in range(2, digits):
                            if digits % i == 0:
                                factors.append(i)
                    for f in factors:
                        if not found:
                            segs = []
                            num_seg = digits // f
                            for i in range(num_seg):
                                segs.append(start[(i*f):((i*f)+f)])
                            num_equal = 0
                            for seg in segs:
                                if seg == segs[0]:
                                    num_equal += 1
                            if num_equal == len(segs):
                                add_ids += int(start)
                                found = True
                    start = str(int(start) + 1)
                else:
                    start = str(10)
                
                save_digits = digits
            print(ran, factors)

        print(add_ids)

sol2()





