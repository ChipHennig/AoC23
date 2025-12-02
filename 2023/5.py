f = open("input.txt", "r")
line = f.readline()
col = line.index(":") + 2
init_s = line[col:-1].split()
ranges = []
for i in range(len(init_s) - 1):
    start = int(init_s[i])
    end = int(init_s[i + 1])
    ranges.append((start, start + end - 1))
it = iter(init_s)
ranges = list(zip(it, it))
seed_rs = [(int(r[0]), int(r[0]) + int(r[1]) - 1) for r in ranges]
line = f.readline()
seed_rs = sorted(seed_rs)


def intersect(x, y):
    x_seeds = (max(x[0], y[0]), min(x[1], y[1]))
    if x_seeds[0] > x_seeds[1]:
        return False
    return x_seeds


while line:
    line = f.readline()
    line = f.readline()
    new_seeds = []
    while line != "\n" and line:
        d_start, src_start, r_len = line.split()
        d_start, src_start, r_len = int(d_start), int(src_start), int(r_len)
        to_remove = []
        for i, r in enumerate(seed_rs):
            org_r = (int(seed_rs[i][0]), int(seed_rs[i][1]))
            src_r = (src_start, src_start + r_len - 1)
            x_seeds = intersect(org_r, src_r)
            is_done = False
            if x_seeds:
                to_remove.append(i)
                if org_r[0] < x_seeds[0]:
                    seed_rs.append((org_r[0], x_seeds[0] - 1))
                if org_r[1] > x_seeds[1]:
                    pos = (x_seeds[1] + 1, org_r[1])
                    seed_rs.append(pos)
                    is_done = True
                dist = x_seeds[0] - src_start
                new_r = (d_start + dist, d_start + x_seeds[1] - x_seeds[0] + dist)
                new_seeds.append(new_r)
            elif org_r[0] > src_r[1]:
                is_done = True
            if is_done:
                break
        line = f.readline()
        for i in reversed(to_remove):
            del seed_rs[i]
        seed_rs = sorted(seed_rs)
    seed_rs += new_seeds
    seed_rs = sorted(seed_rs)
    print(seed_rs)

print(min(seed_rs))
