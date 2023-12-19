def find_dig_volume(filename):  #solution: 97874103749720
    instructions = []
    dirs = ["R", "D", "L", "U"]
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()[-1]
            dir = dirs[int(line[-2])]
            nums = int(line[2:-2],16)
            #print(dirs[dir], nums)
            instructions.append([dir, nums])
    
    print(instructions)
    vertices = generate_vertices(instructions)
    print(vertices)
    #grid = generate_grid(instructions)
    #area_sum = find_fill_area(grid)
    area_sum = calculate_area(vertices) #internal points
    border_points = sum(i[1] for i in instructions)
    return area_sum + border_points/2 + 1


def generate_vertices(instruction):
    vertices = []
    s = [0,0]
    for i in instruction:
        if i[0] == "R":
            s[0] += i[1]
        elif i[0] == "D":
            s[1] += i[1]
        elif i[0] == "L":
            s[0] -= i[1]
        elif i[0] == "U":
            s[1] -= i[1]
        vertices.append(s.copy())
    return vertices

def calculate_area(vertices):
    area = 0
    for i in range(-1,len(vertices)-1):
        area += (vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0])
    print(area)
    return area // 2

def generate_grid(instructions):
    grid = [["."]]
    grid_dims = [1,1]
    head = [0,0]
    for i in instructions:
        print(i)
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
