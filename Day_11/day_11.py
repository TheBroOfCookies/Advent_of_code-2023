def find_galaxy_distance(filename): #solution: 10422930
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            modified_line = []
            for elem in line.strip():
                modified_line.append(elem)
            grid.append(modified_line)
        
    grid = expand_horizontal(grid)
    grid = expand_vertical(grid)
    grid_print(grid)
    grid, galaxy_coords = exchange_to_numbers(grid)
    grid_print(grid)
    return calculate_dist(galaxy_coords)
            
def expand_horizontal(grid):
    modified_grid = grid.copy()
    i = 0
    while i < len(modified_grid):
        expand = True
        for elem in modified_grid[i]:
            if elem == "#":
                expand = False
                break
        if expand:
            modified_grid.insert(i, ["."]*len(grid[0]))
            i+= 1
        i+= 1
    return modified_grid
            
def expand_vertical(grid):
    modified_grid = grid.copy()
    j = 0
    while j < len(modified_grid[0]):
        expand = True
        for i in range(len(grid)):
            if grid[i][j] == "#":
                expand = False
                break
        if expand:
            for i in range(len(modified_grid)):
                modified_grid[i].insert(j+1, ".")
            j += 1
        j+= 1
    return modified_grid

def exchange_to_numbers(grid):
    galax_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                galax_coords.append([i, j])
                grid[i][j] = str(len(galax_coords))
    return grid, galax_coords

def calculate_dist(galaxy_coords):
    print(galaxy_coords)
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