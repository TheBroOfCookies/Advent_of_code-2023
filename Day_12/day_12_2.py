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
            groups = list(map(lambda x: int(x), groups))
            
            springs, groups = expand_springs_groups(springs, groups)
            
            print(springs, groups)

            #criteria = find_criteria(groups)
            criteria = find_criteria(groups)
            partial = check_combination(springs, criteria)
            combos += partial
            line_num += 1
            print("Partial sum:", combos, "  part:", partial, "   Line:", line_num)
            
        return combos

@lru_cache(maxsize=None)
def check_combination(springs, criteria):
    sum = 0
    if ":" in springs:
        springs_check = re.sub(":", "#", springs, 1)
        if re.search(criteria, springs_check):
            sum += check_combination(springs_check, criteria)
        springs_check = re.sub(":", ".", springs, 1) 
        if re.search(criteria, springs_check):
            sum += check_combination(springs_check, criteria)
    else:
        return 1
    if sum > 1000000:
        print(sum)
    return sum

def find_criteria(groups):
    criteria = "^[\.:]*"
    for g in groups[:-1]:
        criteria += "[#:]"*g + "[\.:]+"
    criteria += "(" + "[#:]"*groups[-1] + "[\.:]*)$"
    return criteria

def shorten(springs, criteria):
    crit_b = "".join(criteria.split("[\.:]+")[1:])
    crit_a = criteria.split("[\.:]+")[0]
    crit_a = re.sub("[#:]", "#", crit_a)
    crit_a = "^(" + crit_a + ")"
    if re.search(crit_a, springs):
        return re.sub(crit_a, "", springs, 1), crit_b

def expand_springs_groups(springs, groups):
    springs += ":"
    springs = springs*5
    return springs[:-1], groups*5

#print(find_arragements("test.txt")) #solution: 2517 for task 2
#print(find_arragements("example.txt"))    #solution: 525152 for task 2
#print(find_arragements("input_line_1.txt"))
print(find_arragements("input.txt"))

#print(re.search("#.#", ".#.#."))