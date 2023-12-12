f = open("input.txt", "r")
line = f.readline()
dirs = line[:-1]

f.readline()
line = f.readline()

nodes = {}
start_nodes = []

while line:
    node, adj = line[:-1].split(" = ")
    l, r = adj.replace("(", "").replace(")", "").split(", ")
    nodes.update({node: (l, r)})
    if node[-1] == "A":
        start_nodes.append(node)
    line = f.readline()

init_nodes = start_nodes.copy()
steps = 0
done = False
z_saves = [0] * len(init_nodes)
saves = []
save_steps = []

from math import lcm

while not done:
    for d in dirs:
        for i, n in enumerate(start_nodes):
            c = nodes[n]
            if n[-1] == "Z":
                if z_saves[i] == 0:
                    z_saves[i] = steps
                start_nodes[i] = init_nodes[i]
            elif d == "L":
                start_nodes[i] = c[0]
            else:
                start_nodes[i] = c[1]
        steps += 1
    flags = [n for n in z_saves if n != 0]
    if len(flags) == len(start_nodes):
        done = True
    print(steps)

print(lcm(*z_saves))
