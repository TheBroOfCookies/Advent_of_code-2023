
def find_dig_volume(filename):  #solution: 36725
    grid = [["."]]
    instructions = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            instructions.append([line[0], int(line[1])])
    
    print(instructions)
    grid = generate_grid(instructions)
    area_sum = find_fill_area(grid)
    return area_sum

def generate_grid(instructions):
    grid = [["."]]
    grid_dims = [1,1]
    head = [0,0]
    for i in instructions:
        if i[0] == "R":
            for j in range(i[1]):
                head[1] += 1
                grid, grid_dims = test_and_expand(grid, head, grid_dims)
                grid[head[0]][head[1]] = "#"
        if i[0] == "D":
            for j in range(i[1]):
                head[0] +=1
                grid, grid_dims = test_and_expand(grid, head, grid_dims)
                grid[head[0]][head[1]] = "#"
        if i[0] == "L":
            for j in range(i[1]):
                head[1] -= 1
                grid, grid_dims = test_and_expand(grid, head, grid_dims)
                if head[1] < 0:
                    head[1]  = 0
                grid[head[0]][head[1]] = "#"
        if i[0] == "U":
            for j in range(i[1]):
                head[0] -=1
                grid, grid_dims = test_and_expand(grid, head, grid_dims)
                if head[0] < 0:
                    head[0]  = 0
                grid[head[0]][head[1]] = "#"
            
    return grid
    
def test_and_expand(grid, pos, grid_dims):
    if pos[0] >= grid_dims[0]:
        grid.append(["."]*grid_dims[1])
        grid_dims[0] += 1
    elif pos[0] < 0:
        grid.insert(0, ["."]*grid_dims[1])
        grid_dims[0] += 1
    elif pos[1] >= grid_dims[1]:
        for l in grid:
            l.append(".")
        grid_dims[1] += 1
    elif pos[1] < 0:
        for l in grid:
            l.insert(0, ".")
        grid_dims[1] += 1
    return grid, grid_dims

def find_fill_area(grid):
    filled_grid = fill_grid(grid)
    grid_print_to_file(filled_grid, "output.txt")
    return sum(1 if s == "#" else 0 for l in grid for s in l)
        
def fill_grid(grid):
    grid_dims = [len(grid), len(grid[0])]
    backlog = [[1,75]]
    while len(backlog):
        b = backlog.pop(0)
        b_explore = [[b[0], b[1]+1], [b[0]+1, b[1]], [b[0], b[1]-1], [b[0]-1, b[1]]]
        for b_r in b_explore:
            if b_r[0] < 0 or b_r[0] >= grid_dims[0] or b_r[1] < 0 or b_r[1] >= grid_dims[1]:
                continue
            if b_r in backlog:
                continue
            if grid[b_r[0]][b_r[1]] == "#":
                continue
            else:
                grid[b_r[0]][b_r[1]] = "#"
                backlog.append(b_r)
                
    return grid

def grid_print_to_file(grid, filename):
    g_p = ["".join(l) for l in grid]
    with open(filename, "w") as file:
        file.write("\n".join(g_p))
    
    
#print(find_dig_volume("example.txt"))
print(find_dig_volume("input.txt"))
