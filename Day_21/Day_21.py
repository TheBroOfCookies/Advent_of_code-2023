def find_number_of_plots(filename):  #solution: 3660
    grid = []
    with open(filename) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))
    grid_print(grid)
    start = get_start(grid)
    print(start)
    reached = step(grid, start, 64)
    grid_print_steps(grid, reached)
    print(reached)
    return len(reached)


def step(grid, start, steps):
    print("Steps",steps)
    q = [start]
    dirs=((0,1), (1,0), (0,-1), (-1,0))
    for i in range(steps):
        next_q = []
        while len(q):
            x, y = q.pop()
            for dir in dirs:
                xx, yy = offset(x,y,dir)
                if grid[yy][xx] != "#":
                    next_q.append((xx,yy))
        q = list(set(next_q))
    return q

def get_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return i, j

def offset(x,y,dir):
    return x+dir[0], y+dir[1]            

def grid_print(grid):
    for l in grid:
        for s in l:
            print(s, end="") 
        print()
    print()
    
def grid_print_steps(grid, reached):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
           if (j,i) in reached:
               print("O", end="")
           else:
               print(grid[i][j], end="")
        print()
    print()
                
#print(find_number_of_plots("example.txt")) #expected: 16
print(find_number_of_plots("input.txt"))