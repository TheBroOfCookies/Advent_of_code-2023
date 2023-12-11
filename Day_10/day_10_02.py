class GridPoint:
    def __init__(self, left, top, right, down, sym):
        self.left = left
        self.right = right
        self.top = top
        self.down = down
        self.sym = sym
        self.prev = [-1,-1]
        self.status = 0
        
    def __str__(self):
        return str(self.status)

start_coords = [-1,-1]
def find_animal(filename):
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            line = parse_line(line)
            if start_coords[0] == -1 and start_coords[1] != -1:
                start_coords[0] = i
            grid.append(line)
    if start_coords == [-1,-1]:
        print("Wrong starting coords")
        return -1
    else:
        print("Starting point:", start_coords)

    return BFS_search(start_coords, grid)


def parse_line(line):
    parsed = []
    for j in range(len(line)):  #Left, top, right, down
        if line[j] == "|":
            parsed.append(GridPoint(False, True, False, True, line[j]))
        elif line[j] == "-":
            parsed.append(GridPoint(True, False, True, False, line[j]))
        elif line[j] == "L":
            parsed.append(GridPoint(False, True, True, False, line[j]))
        elif line[j] == "J":
            parsed.append(GridPoint(True, True, False, False, line[j]))
        elif line[j] == "7":
            parsed.append(GridPoint(True, False, False, True, line[j]))
        elif line[j] == "F":
            parsed.append(GridPoint(False, False, True, True, line[j]))
        elif line[j] == ".":
            parsed.append(GridPoint(False, False, False, False, line[j]))
        elif line[j] == "S":
            parsed.append(GridPoint(True, True, True, True, line[j]))
            start_coords[1] = j

    return parsed

def BFS_search(start, grid):
    sx, sy = start
    frontier = [[sx, sy]]
    while len(frontier) > 0:
        print_grid_both(grid)
        #print_frontier(frontier, grid)
        next_search = frontier.pop(0)
        frontier += BFS_search_neighbors(grid, next_search)
        #if duplicates(frontier):
        #    print("Frontier with dupe", frontier)
        #    break
    
    find_enclosed(grid)
    print_grid_both(grid)
    
    sum = 0     
    for line in grid:
        for elem in line:
            if elem.status == 8:
                sum += 1
    return sum

def BFS_search_neighbors(grid, coords):
    y, x = coords
    prev = grid[y][x].prev
    grid[y][x].status = 2
    legal_neighbors = []
    try:
        if grid[y+1][x].top and grid[y][x].down and [y+1, x] != prev:
            legal_neighbors.append([y+1, x])
            grid[y+1][x].prev = [y,x]
    except:
        pass
    try:
        if grid[y-1][x].down and grid[y][x].top and [y-1, x] != prev:
            legal_neighbors.append([y-1, x])
            grid[y-1][x].prev = [y,x]
    except:
        pass
    try:
        if grid[y][x+1].left and grid[y][x].right and [y, x+1] != prev:
            legal_neighbors.append([y, x+1])
            grid[y][x+1].prev = [y,x]
    except:
        pass
    try:
        if grid[y][x-1].right and grid[y][x].left and [y, x-1] != prev:
            legal_neighbors.append([y, x-1])
            grid[y][x-1].prev = [y,x]
    except:
        pass
    
    for l in legal_neighbors:
        if grid[l[0]][l[1]].status == 2:
            return []
        else:
            grid[l[0]][l[1]].status = 1

    return legal_neighbors

def duplicates(frontier):
    for i in range(len(frontier)):
        for j in range(len(frontier)):
            if j != i:
                if frontier[i] == frontier[j]:
                    print("Found duplicate:", frontier[i])
                    return frontier[i]
    return 0

def grid_prev(grid, y, x):
    return grid[y][x].prev

def print_grid(grid):
    for line in grid:
        for elem in line:
            print(elem, end="")
        print()
    print()
    
def print_grid_symbol(grid):
    for line in grid:
        for elem in line:
            print(elem.sym, end="")
        print()
    print()
    
def print_grid_both(grid):
    for line in grid:
        for elem in line:
            if(elem.status == 8):
                print("`", end="")
            elif(elem.status > 0):
                print(elem, end="")
            else:
                print(".", end="")
        print(" ", end="\t")
        for elem in line:
            print(elem.sym, end="")
        print()
    print()
        
def print_frontier(frontier, grid):
    print("F:",frontier)
    print("P:  ", end = "")
    for f in frontier:
        print(grid[f[0]][f[1]].prev, end = "  ")
    print()
    
    
def find_enclosed(grid):
    prev_el = GridPoint(False, False, False, False, "/")
    for line in grid:
        flip = -1
        for elem in line:
            if elem.status == 2 and not prev_el.right:
                flip *= -1
            elif elem.status == 2 and not elem.right:
                flip *= -1
            elif elem.status != 2:
                elem.status += 4*flip
            prev_el = elem
            
    prev_el = GridPoint(False, False, False, False, "/")
    for j in range(len(grid[0])):
        flip = -1
        for i in range(len(grid)):
            if grid[i][j].status == 2 and not prev_el.down:
                flip *= -1
            elif grid[i][j].status == 2 and not grid[i][j].down:
                flip *= -1
            elif grid[i][j].status != 2:
                grid[i][j].status += 4*flip
            prev_el = grid[i][j]
            
#print(find_animal("example.txt"))
#print(find_animal("example2.txt"))
#print(find_animal("example3.txt"))
print(find_animal("example5.txt"))
#print(find_animal("input.txt"))