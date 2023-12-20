def find_number_of_signals(filename):  #solution: 739960225
    units = {}
    unit_to_category = {}
    conjunctors = {}
    flip_flops = {}
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            src, dest = list(map(lambda x: x.strip(), line.strip().split("->")))
            if src != "broadcaster":
                if src[0] == "&":
                    conjunctors[src[1:]] = {}
                    unit_to_category[src[1:]] = "&"
                elif src[0] == "%":
                    flip_flops[src[1:]] = False
                    unit_to_category[src[1:]] = "%"
                units[src[1:]] = list(map(lambda x: x.strip(), dest.split(",")))
            else: 
                units[src] = list(map(lambda x: x.strip(), dest.split(",")))
                
    
    for c in conjunctors.keys():
        for k in units.keys():
            if c in units[k]:
                conjunctors[c][k] = False
                
    print([(k, units[k]) for k in units.keys()])
    print([(k, unit_to_category[k]) for k in unit_to_category.keys()])
    print([(k, conjunctors[k]) for k in conjunctors.keys()])
    print([(k, flip_flops[k]) for k in flip_flops.keys()])
    print()
    sig_low, sig_high = 0,0
    for i in range(0, 1000):
        conjunctors, flip_flops, sig_low, sig_high = propagate_signals(units, unit_to_category, conjunctors, flip_flops, sig_low, sig_high)
    
    print()
    print([(k, conjunctors[k]) for k in conjunctors.keys()])
    print([(k, flip_flops[k]) for k in flip_flops.keys()])
    print(sig_low, sig_high)
    
    return sig_low * sig_high

def propagate_signals(units, unit_to_category, conjuctors, flip_flops, sig_low, sig_high):
    backlog = []
    cons = conjuctors.keys()
    sig_low += 1
    for start in units["broadcaster"]:
        backlog.append((start, False)) #low = False, high = True
        sig_low += 1
    while len(backlog):
        src, sig = backlog.pop(0)
        if src == "output" or src =="rx":
            continue
        category = unit_to_category[src]
        if category == "%":
            if not sig:
                flip_flops[src] = not flip_flops[src] #flip flip_flop
                for dest in units[src]:
                    if flip_flops[src]:
                        sig_high += 1
                    else:
                        sig_low += 1
                    backlog.append((dest, flip_flops[src]))
                    if dest in cons:
                        conjuctors[dest][src] = flip_flops[src]
        elif category == "&":
            all_high = all(conjuctors[src].values())
            
            for dest in units[src]:
                if not all_high:
                    sig_high += 1
                else:
                    sig_low += 1
                backlog.append((dest, not all_high))  #if all high, send low, otherwise send high
                if dest in cons:
                    conjuctors[dest][src] = not all_high
            
        else:
            print("Error")
    return conjuctors, flip_flops, sig_low, sig_high
    
                
#print(find_number_of_signals("example.txt")) #expected: 32000000
#print(find_number_of_signals("example2.txt")) #expected: 11687500
print(find_number_of_signals("input.txt"))