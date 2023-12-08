def find_steps_to_xxz(filename): #solution: 13663968099527
    directions = ""
    current_nodes = []
    map_left = {}
    map_right = {}
    with open(filename) as file:
        lines = file.readlines()
        directions = lines[0].strip()
        for line in lines[2:]:
            name, rest = line.strip().split("=")
            name = name.strip()
            left, right = rest.replace("(", "").replace(")", "").split(",")
            map_left[name] = left.strip()
            map_right[name] = right.strip()
            if "A" in name:
                current_nodes.append(name)
    #print(map_left)
    #print(map_right)
    steps_to_goal =[]
    start_nodes = current_nodes.copy()
    for i in range(len(start_nodes)):
        steps = 0
        node_to_check = start_nodes[i]
        searching = True
        while searching:
            for d in directions:
                if d == "L":
                    node_to_check = map_left[node_to_check]
                else: 
                    node_to_check = map_right[node_to_check]
                steps += 1
                if "Z" in node_to_check:
                    searching= False
                    steps_to_goal.append(steps)
                    break
                    
    return steps_to_goal
 
#print(find_zzz("example2.txt"))
steps = (find_steps_to_xxz("input.txt"))
#steps = [13939, 17621, 11309, 20777, 19199, 15517]
print(steps)
x = steps[0]
dx = steps[0]
for y in steps[1:]:
    dy = y
    print(x)
    while x != y:
        if x > y:
            y += dy
        else:
            x += dx
    dx = x
print(x)