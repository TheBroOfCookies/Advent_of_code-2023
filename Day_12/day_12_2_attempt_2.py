import re 
from functools import lru_cache

def find_arragements(filename):
    with open(filename) as file:
        lines = file.readlines()
        combos = 0
        line_num = 0
        for line in lines:
            springs, groups = line.strip().split()
            springs = "".join(list(map(lambda x: ":" if x == "?" else x, springs)))
            springs = re.sub("\.+", ".", springs)
            groups = groups.split(",")
            groups = "".join(groups)
            
            springs, groups = expand_springs_groups(springs, groups)
            
            print(springs, groups)

            #criteria = find_criteria(groups)
            criteria = find_criteria(groups)
            partial = check_combination(springs, criteria, groups)
            combos += partial
            line_num += 1
            print("Partial sum:", combos, "  part:", partial, "   Line:", line_num)
            
        return combos

@lru_cache(maxsize=None)
def check_combination(springs, criteria, groups):
    springs, criteria, groups = shorten(springs, criteria, groups)
    sum = 0
    if ":" in springs:
        springs_check = re.sub(":", "#", springs, 1)
        if re.search(criteria, springs_check):
            sum += check_combination(springs_check, criteria, groups)
        springs_check = re.sub(":", ".", springs, 1) 
        if re.search(criteria, springs_check):
            sum += check_combination(springs_check, criteria, groups)
    else:
        return 1
    #if sum > 1000000:
    #    print(sum)
    return sum
@lru_cache(maxsize=None)
def find_criteria(groups):
    criteria = "^[\.:]*"
    for g in groups[:-1]:
        criteria += "[#:]"*int(g) + "[\.:]+"
    criteria += "(" + "[#:]"*int(groups[-1]) + "[\.:]*)$"
    return criteria

""" 
def shorten(springs, criteria):
    crit_b = "^[\.:]*" +"[\.:]+".join(criteria.split("[\.:]+")[1:])
    crit_a = criteria.split("[\.:]+")[0]
    #crit_a = re.sub(r"^[\.:]*", "^[\.]*", crit_a, 1)
    crit_a.replace("^[\.:]*", "^[\.]*", 1)
    crit_a.replace("[#:]", "#", 1)
    crit_a += ":?"
    print(criteria)
    print(crit_a)
    print(crit_b)
    if re.search(crit_a, springs):
        return re.sub(crit_a, "", springs, 1), crit_b
    return springs, criteria
"""
@lru_cache(maxsize=None)
def shorten(springs, criteria, groups):
    crit_a = find_criteria(groups[0])
    if re.search(crit_a, springs):
        crit_b = find_criteria(groups[1:])
        return re.sub(crit_a, "", springs, 1), crit_b, groups[1:]
    return springs, criteria, groups
    

def expand_springs_groups(springs, groups):
    springs += ":"
    springs = springs*5
    return springs[:-1], groups*5

#print(find_arragements("test.txt")) #solution: 2517 for task 2
print(find_arragements("example.txt"))    #solution: 525152 for task 2
#print(find_arragements("example1.txt"))    #solution: 16384 for task 2
#print(find_arragements("input_line_1.txt"))
#print(find_arragements("input.txt"))

#print(re.search("#.#", ".#.#."))
"""
s = ".#.######.#####.:::::.######.#####.:::::.######.#####.:::::.######.#####.:::::.######.#####."
g = "".join(map(lambda x: str(x), [1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5]))
c = find_criteria(g)
print(s,c)
s, c = shorten(s,c, g)
print(s,c)
"""
#print(check_combination(s,c))

