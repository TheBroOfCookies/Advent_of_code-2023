from bricks import bricks #hard coded bricks after falling to spare time

def find_disintegratable_bricks(filename): #solution 432
    """ 
    bricks = []
    with open(filename) as file:
        for line in file.readlines():
            line = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), line.strip().split("~")))
            bricks.append(line)
    bricks= apply_gravity(bricks)
    """
    deps = generate_dependencies(bricks)
    sum = check_disintegration(bricks, deps)
    return sum


def apply_gravity(bricks):
    change = True
    i = 0
    print("Initializing Bricks")
    while change:
        if i % 7 == 0:
            print(round(i/140*100, 1), "% done Initializing")
        i += 1
        change = False
        for cs, ce in bricks:
            if cs[2] == 1 or ce[2] == 1:
                    continue
            can_fall = True
            for s,e in bricks:
                if cs == s and ce == e:
                    continue
                cs1, ce1 = cs.copy(), ce.copy()
                cs1[2] -= 1
                ce1[2] -= 1
                if intersect_range([cs1,ce1], [s,e]):
                    can_fall = False
                    break
            if can_fall:
                cs[2] -= 1
                ce[2] -= 1
                change = True
    print("Initialization complete\n")
    return bricks


def generate_dependencies(bricks):
    dependencies = {}
    print("Generating dependencies")
    for i in range(len(bricks)):
        if i % 125 == 0:
            print(round(i/1250*100, 1), "% done generating")
        cs, ce = bricks[i]
        dependencies[i] = []
        if cs[2] == 1 or ce[2] == 1:
                continue
        for s,e in bricks:
            if cs == s and ce == e:
                continue
            cs1, ce1 = cs.copy(), ce.copy()
            cs1[2] -= 1
            ce1[2] -= 1
            if intersect_range([cs1,ce1], [s,e]):
                dependencies[i].append([s,e])
    print("Generation complete\n")
    return dependencies

def is_stable(bricks, i, deps):
    brick = bricks[i]
    for k in deps.keys():
        if k == i:
            continue
        cs, ce = bricks[k]
        if cs[2] < 2 or ce[2]  < 2:
            continue
        if (brick) in deps[k]:
            if len(deps[k]) <= 1:
                return False
        
    return True

def check_disintegration(bricks, deps):
    sum = 0
    print("Testing disintegration")
    for i in range(len(bricks)):
        if i % 125 == 0:
            print(round(i/1250*100, 1), "% done testing")
        if is_stable(bricks, i, deps):
            sum += 1
    print("Testing complete\n")
    return sum

def intersect_range(b1, b2):
    s1, e1 = b1
    s2, e2 = b2
    for x in range(max(s1[0], s2[0]), min(e1[0], e2[0])+1):
        for y in range(max(s1[1], s2[1]), min(e1[1], e2[1])+1):
            for z in range(max(s1[2], s2[2]), min(e1[2], e2[2])+1):
                return True
    return False


#print(find_disintegratable_bricks("example.txt")) #expected: 5
print(find_disintegratable_bricks("input.txt"))
