def find_crossing_paths(filename, lims): #solution: 21679
    print("Reading from file...")
    flakes = []
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip().split("@")
            pos, vel = list(map(lambda x: x.strip().split(","), line))
            pos = tuple(map(lambda x: int(x), pos))
            vel = tuple(map(lambda x: int(x), vel))
            flakes.append((pos[0:2], vel[0:2]))  #ignore Z
    print(flakes)
    intersects = 0
    for i in range(len(flakes)):
        f1 = flakes[i]
        for f2 in flakes[i+1:]:  #i+1 to void checking a line against itself
            if check_intersect(f1, f2, lims):
                intersects += 1
    return intersects

def check_intersect(f1, f2, lims):
    pos1, vel1 = f1
    vx1, vy1 = vel1

    pos2, vel2 = f2
    vx2, vy2 = vel2

    if vy1/vx1 == vy2/vx2:
        return False
    
    x1s, y1s, x1e, y1e = find_limit(pos1, vel1, lims)
    x2s, y2s, x2e, y2e = find_limit(pos2, vel2, lims)
    
    return intersect((x1s, y1s),(x1e, y1e), (x2s, y2s), (x2e, y2e))
    


def find_limit(start, deriv, limits):  #finds minimum and maximum values for the line segment withing the limit ahead in time
    x,y = correct_starting_values(start, deriv, limits)
    dx, dy = deriv
    lim_l, lim_h = limits

    t = min(max((lim_h-x)/dx, (lim_l-x)/dx), max((lim_h-y)/dy, (lim_l-y)/dy))
    return (x, y, x+dx*t, y+dy*t)

def correct_starting_values(start, deriv, limits):
    x,y = start
    dx, dy = deriv
    lim_l, lim_h = limits

    if x > lim_h:
        if dx > 0:
            return (0,0)
        y  = y+dy*(lim_h-x)/dx
        x = lim_h
    elif x < lim_l:
        if dx < 0:
            return (0,0)
        y  = y+dy*(lim_l-x)/dx
        x = lim_l

    if y > lim_h:
        if dy > 0:
            return (0,0)
        x  = x+dx*(lim_h-y)/dy
        y = lim_h
    elif y < lim_l:
        if dy < 0:
            return (0,0)
        x  = x+dx*(lim_l-y)/dy
        y = lim_l




def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


    


# limits = (7,27)
# print(find_crossing_paths("example.txt", limits)) #expected: 2
limits = (200000000000000, 400000000000000)
print(find_crossing_paths("input.txt", limits))  #21679 actuall

