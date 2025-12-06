import math

data = open("input.txt", "r")

def sol1():
    with open("input.txt", "r") as f:
        content = f.readlines()

        total = 0

        for line in content:
            print(line)
            v_max_idx = 0
            v_max = 0
            for i in range(len(line) - 1):
                if int(line[i]) > v_max:
                    v_max = int(line[i])
                    v_max_idx = i

            second_max = 0
            second_range = range(v_max_idx + 1, len(line) - 1)
            if v_max_idx == len(line) - 2:
                second_range = range(len(line) - 2)
            
            for i in second_range:
                if int(line[i]) > second_max:
                    second_max = int(line[i])

            if v_max_idx == len(line) - 2:
                t_max = v_max
                v_max = second_max
                second_max = t_max
            
            volts = int(str(v_max) + str(second_max))

            print(volts)

            total += volts
        
        print(total)

def sol2():
    with open("input.txt", "r") as f:
        content = f.readlines()
        total = 0
        for line in content:
            prev_idx = -1
            nums = []
            line = line.strip()
            for i in reversed(range(12)):
                sub_max = 0
                for j in range(prev_idx + 1, len(line) - i):
                    if int(line[j]) > sub_max:
                        sub_max = int(line[j])
                        prev_idx = j
                nums.append(sub_max)
            number = "".join(map(str, nums))
            total += int(number)

        print(total)

sol2()