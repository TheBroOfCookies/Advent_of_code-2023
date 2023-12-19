def find_rating_combinations(filename):  #solution: 116138474394508
    instructions = {}
    parts = []
    xmas_tup = ("x", "m", "a", "s")
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
                        check.append((xmas_tup.index(c1[0]), c1[1], int(c1[2:]), c2))
                    else:
                        check.append((c))
                instructions[key] = check
            elif line == "\n":
                break
            
    return sort_part_range([(1, 4000),(1, 4000),(1, 4000),(1, 4000)], instructions)

def sort_part_range(part, instructions):
    xmas_tup = ("x", "m", "a", "s")
    flow = []
    sum = 0
    backlog = [(part, "in")]
    while len(backlog):
        i = 0
        part, dest = backlog.pop(0)
        if dest == "R":
            flow = []
        elif dest == "A":
            sum += combos(part)
            flow = []
        else:
            flow = instructions[dest]
        while i < len(flow):
            if len(flow[i]) != 4: #last element in flow, all cases accepted
                if flow[-1] == "R":
                    break
                elif flow[-1] == "A":
                    sum += combos(part)
                    break
                flow = instructions[flow[-1]]
                i = 0
                continue
            xmas, crit, val, dest = flow[i]
            start, end = part[xmas]
            if crit == "<":   
                if part[xmas][1] < val: #case 2
                    if dest == "R":
                        break
                    if dest == "A":
                        sum += combos(part)
                        break
                    flow = instructions[dest]
                    i = 0
                    continue
                elif start < val: #case 1
                    new_part = [part[0], part[1], part[2], part[3]]
                    new_part[xmas] = (start, val-1) #segment < val is sent to backlog (excluding val since val !< val)
                    backlog.append((new_part, dest))
                    part[xmas] = (val, end) #segment >= val is computed further
                    
            elif crit == ">": 
                if start > val: #case 4
                    if dest == "R":
                        break
                    if dest == "A":
                        sum += combos(part)
                        break
                    flow = instructions[dest]
                    i = 0
                    continue
                elif end > val: #case 3
                    new_part = [part[0], part[1], part[2], part[3]]
                    new_part[xmas] = (val+1, end) #segment > val is sent to backlog (excluding val since val !> val)
                    backlog.append((new_part, dest))
                    part[xmas] = (start, val)  #segment <= val is computed further
            else:
                print("Illegal criteria", crit)
            i += 1
    return sum
                
def combos(part):
    comb = 1
    for p in part:
        comb *= p[1]-p[0]+1
    return comb
            

#print(find_rating_combinations("example.txt")) #expected: 167409079868000
print(find_rating_combinations("input.txt"))
            