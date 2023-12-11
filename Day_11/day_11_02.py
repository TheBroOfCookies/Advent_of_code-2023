def find_galaxy_distance(filename): #solution: 699909023130
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            modified_line = []
            for elem in line.strip():
                modified_line.append(elem)
            grid.append(modified_line)
        
    rows = expand_horizontal(grid)
    cols = expand_vertical(grid)
    print(rows, cols)
    #grid_print(grid)
    galaxy_coords = get_galaxy_coords(grid, rows, cols)
    return calculate_dist(galaxy_coords)
            
def expand_horizontal(grid):
    expanded_rows = []
    i = 0
    for i in range(len(grid)):
        expand = True
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                expand = False
                break
        if expand:
            expanded_rows.append(i)
    return expanded_rows
            
def expand_vertical(grid):
    expanded_cols = []
    i = 0
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            expand = True
            if grid[i][j] == "#":
                expand = False
                break
        if expand:
            expanded_cols.append(j)
    return expanded_cols

def get_galaxy_coords(grid, rows, cols):
    galax_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                ci = i
                cj = j
                for k in rows:
                    if i > k:
                        ci += 1000000 - 1
                for l in cols:
                    if j > l:
                        cj += 1000000 - 1
                galax_coords.append([ci, cj])
    return galax_coords

def calculate_dist(galaxy_coords):
    sum = 0
    for i in range(len(galaxy_coords)):
        for j in range(i+1, len(galaxy_coords)):
            sum += abs(galaxy_coords[i][0] - galaxy_coords[j][0])
            sum += abs(galaxy_coords[i][1] - galaxy_coords[j][1])
    return sum
        

def grid_print(grid):
    for line in grid:
        for elem in line:
            print(elem, end="")
        print()
    print() 


#print(find_galaxy_distance("example.txt"))
print(find_galaxy_distance("input.txt"))