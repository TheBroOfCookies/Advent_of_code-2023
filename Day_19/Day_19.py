def find_rating_sum(filename):  #solution: 280909
    instructions = {}
    parts = []
    xmas = ("x", "m", "a", "s")
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if ":" in line:
                key, checks = line.strip().split("{")
                checks = checks[:-1].split(",")
                check = []
                for c in checks:
                    if ":" in c:
                        c1, c2 = c.split(":")
                        check.append((xmas.index(c1[0]), c1[1], int(c1[2:]), c2))
                    else:
                        check.append((c))
                instructions[key] = check
            elif line == "\n":
                pass
            else:
                line = line.strip()[1:-1]
                line = line.split(",")
                p = []
                for l in line:
                    p.append(int(l.split("=")[1]))
                parts.append(p)
    return sum(sort_part(p, instructions) for p in parts)

def sort_part(part, instructions):
    flow = instructions["in"]
    while True:
        for i in range(len(flow)):
            if len(flow[i]) != 4:
                if flow[-1] == "R":
                    return 0
                elif flow[-1] == "A":
                    return sum(part)
                flow = instructions[flow[-1]]
                break
            xmas, crit, val, dest = flow[i]
            if crit == "<":
                if part[xmas] < val:
                    if dest == "R":
                        return 0
                    if dest == "A":
                        return sum(part)
                    flow = instructions[dest]
                    break
            elif crit == ">":
                if part[xmas] > val:
                    if dest == "R":
                        return 0
                    if dest == "A":
                        return sum(part)
                    flow = instructions[dest]
                    break
            else:
                print("Illegal criteria", crit)
            
        


#print(find_rating_sum("example.txt")) #expected: 19114
print(find_rating_sum("input.txt"))
            