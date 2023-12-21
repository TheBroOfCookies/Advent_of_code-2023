def find_number_of_plots(filename):  #solution: 3744, 33417, 92680
    grid = []
    with open(filename) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))
    grid_print(grid)
    start = (get_start(grid))
    print(start)
    reached, lengs = step(grid, start, 26501365)
    print(lengs)
    return len(reached)


def step(grid, start, steps):
    print("Steps",steps)
    grid_dims = (len(grid), len(grid[0]))
    print(grid_dims[0])
    q = [start]
    dirs=((0,1), (1,0), (0,-1), (-1,0))
    lengs = []
    for i in range(0,steps):
        #if i%grid_dims[0] == steps%grid_dims[0]:
        if i%grid_dims[0] == steps%grid_dims[0]:
            print(i, len(q))
        lengs.append(len(q))
        next_q = []
        while len(q):
            x, y, wx, wy = q.pop(0)
            for dir in dirs:
                xx, yy, wxx, wyy = offset(x,y,dir, wx, wy, grid_dims)
                if grid[yy][xx] != "#":
                    next_q.append((xx,yy, wxx, wyy))
        q = list(set(next_q))
    lengs.append(len(q))
    return q, lengs

def get_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return i, j, 0, 0

def offset(x,y,dir, wx, wy, grid_dims):
    x += dir[1] 
    y += dir[0]
    if x < 0:
        x = grid_dims[1]-1
        wx -= 1
    elif x > grid_dims[1]-1:
        x = 0
        wx += 1
    elif y < 0:
        y = grid_dims[0]-1
        wy -= 1
    elif y > grid_dims[0]-1:
        y = 0
        wy += 1
    return x, y, wx, wy   

def grid_print(grid):
    for l in grid:
        for s in l:
            print(s, end="") 
        print()
    print()

def grid_print_steps(grid, reached):
    reached = list(map(lambda x: x[:2], reached))
    print(reached)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in reached:
                print(reached.count((j,i)), end="")
            else:
               print(grid[i][j], end="")
        print()
    print()
                
#print(find_number_of_plots("example.txt")) #expected: 668697 for 1000 steps, 1594 for 50 steps
print(find_number_of_plots("input.txt"))    #run, wait for three values, interpolate with wolfram