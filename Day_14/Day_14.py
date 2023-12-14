def find_beam_weights(filename):  #solution: 110565
    with open(filename) as file:
        lines = file.readlines()
        grid = []
        for line in lines:
            grid.append(list(line.strip()))
    grid_print(grid)
    move_rocks(grid)
    grid_print(grid)
    return get_load_weight(grid) 
            
def move_rocks(grid):
    moved = False
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O" and grid[i-1][j] == ".":
                grid[i-1][j] = "O"
                grid[i][j] = "."
                moved = True
    if moved:
        grid = move_rocks(grid)
    return grid

def get_load_weight(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                sum += len(grid)-i
    return sum
            
            
def grid_print(grid):
    for i in grid:
        for j in i:
            print(j, end="")
        print()
    print()
    
    
#print(find_beam_weights("example.txt"))
print(find_beam_weights("input.txt"))