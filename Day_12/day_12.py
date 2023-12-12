import re 

def find_arragements(filename):  #solution: 8419
    with open(filename) as file:
        lines = file.readlines()
        combs = 0
        for line in lines:
            springs, groups = line.strip().split()
            springs = list(springs)
            groups = groups.split(",")
            groups = list(map(lambda x: int(x), groups))
            #print(springs, groups)
            unknowns = find_unknowns(springs)
            #print(unknowns)
            combs += check_combination(springs, unknowns, groups)
            
        return combs
            

def find_unknowns(springs):
    unknowns = []
    for i in range(len(springs)):
        if springs[i] == "?":
            unknowns.append(i)
    return unknowns

def check_combination(springs, unknowns, groups):
    springs_check = springs.copy()
    sum = 0
    if len(unknowns) > 0:
        springs_check[unknowns[0]] = "#"
        sum += check_combination(springs_check, unknowns[1:], groups)
        springs_check[unknowns[0]] = "."
        sum += check_combination(springs_check, unknowns[1:], groups)
    elif is_legal_combination(springs, groups):
        return 1
    return sum
        
def is_legal_combination(springs, groups):
    search_criteria = "^\.*"
    for g in groups[:-1]:
        search_criteria += "#"*g + "\.+"
    search_criteria += "(" + "#"*groups[-1] + "\.*)$"
    x = re.search(search_criteria, "".join(springs))
    if x:
        return True
    return False

#print(find_arragements("example.txt"))           
print(find_arragements("input.txt"))