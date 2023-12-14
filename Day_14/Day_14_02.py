rock_pos = []
cube_pos = []
dims = []

def find_beam_weights(filename):  #solution: 89845
    with open(filename) as file:
        lines = file.readlines()
        grid = []
        for line in lines:
            grid.append(list(line.strip()))
    set_rock_pos(grid)
    big_range = 1000000000
    weights = []
    i = 0
    while i < big_range:
        grid = move_rocks_north(grid) #north
        grid = move_rocks_west(grid) #west
        grid = move_rocks_south(grid) #south
        grid = move_rocks_east(grid) #east
        weights.append(get_load_weight(grid))
        loop = check_for_loop(weights)
        if loop:
            print(i, loop, -(big_range-((big_range - i)//loop*loop +1 +i)))
            i = (big_range - i)//loop*loop + 1 + i
            print(i - big_range)
            break
        print(i, "iter done")
        i += 1
    while i < big_range:
        grid = move_rocks_north(grid) #north
        grid = move_rocks_west(grid) #west
        grid = move_rocks_south(grid) #south
        grid = move_rocks_east(grid) #east
        weights.append(get_load_weight(grid))
        print(i, "iter done")
        i += 1
    return get_load_weight(grid) 



def set_rock_pos(grid):
    global rock_pos
    global cube_pos
    global dims
    dims = [len(grid), len(grid[0])]
    for i in range(dims[0]):
        for j in range(dims[1]):
            if grid[i][j] == "O":
                rock_pos.append([i,j])
            elif grid[i][j] == "#":
                cube_pos.append([i,j])
            
def move_rocks_north(grid):
    moved = False
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if i-1 < 0:
                continue
            if grid[i][j] == "O" and grid[i-1][j] == ".":
                grid[i-1][j] = "O"
                grid[i][j] = "."
                moved = True
    if moved:
        grid = move_rocks_north(grid)
    return grid

def move_rocks_south(grid):
    moved = False
    for i in range(len(grid)-1):
        for j in range(len(grid[0])):
            if i+1 > len(grid)-1:
                continue
            if grid[i][j] == "O" and grid[i+1][j] == ".":
                grid[i+1][j] = "O"
                grid[i][j] = "."
                moved = True
    if moved:
        grid = move_rocks_south(grid)
    return grid

def move_rocks_west(grid):
    moved = False
    for i in range(len(grid)):
        for j in range(1,len(grid[0])):
            if j-1 < 0:
                continue
            if grid[i][j] == "O" and grid[i][j-1] == ".":
                grid[i][j-1] = "O"
                grid[i][j] = "."
                moved = True
    if moved:
        grid = move_rocks_west(grid)
    return grid

def move_rocks_east(grid):
    moved = False
    for i in range(len(grid)):
        for j in range(len(grid[0])-1):
            if j+1 > len(grid[0])-1:
                continue
            if grid[i][j] == "O" and grid[i][j+1] == ".":
                grid[i][j+1] = "O"
                grid[i][j] = "."
                moved = True
    if moved:
        grid = move_rocks_east(grid)
    return grid


def get_load_weight(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                sum += len(grid)-i
    return sum
            
def check_for_loop(weights):
    for i in range(2,len(weights)):
        if weights[-i:] == weights[-i*2:-i]:
            return i
    return 

def grid_print(grid):
    for i in grid:
        for j in i:
            print(j, end="")
        print()
    print()
    
#print(check_for_loop([1,2,3,1,2,3,1,2,3]))
#print(find_beam_weights("example.txt"))
print(find_beam_weights("input.txt"))
