f = open("input.txt", "r")
line = f.readline()
dirs = line[:-1]

f.readline()
line = f.readline()

nodes = {}

while line:
    node, adj = line[:-1].split(" = ")
    l, r = adj.replace("(", "").replace(")", "").split(", ")
    nodes.update({node: (l, r)})
    line = f.readline()


start = "AAA"
end = "ZZZ"
current = start
steps = 0
done = False
while not done:
    for i, d in enumerate(dirs):
        c = nodes[current]
        if d == "L":
            current = c[0]
        else:
            current = c[1]
        steps += 1
    if current == end:
        done = True

print(steps)
