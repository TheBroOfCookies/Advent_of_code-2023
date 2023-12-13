def find_mirror_sums(filename):  #solution: 33047
    with open(filename) as file:
        lines = file.readlines()
        sum = 0
        accum = []
        for line in lines:
            if line == "\n" or line == "":
                grid_print(accum)
                h = 0
                hort = 0
                while h < len(accum)-1:
                    h = find_horizontal_mirroring(accum, h)
                    if is_horizontal_mirroring(accum, h):
                        hort = h
                        break
                v = 0
                vert = 0
                while v < len(accum[0])-1:
                    v = find_vertical_mirroring(accum, v)
                    if is_vertical_mirroring(accum, v):
                        vert = v
                        break
                sum += vert + hort*100
                accum = []
                
            else:
                accum.append(line.strip())
                
        return sum
            
            
            
def find_vertical_mirroring(grid, start):
    grid = list(map(lambda x: x[start:], grid))
    grid_print(grid)
    for j in range(len(grid[0])-1):
        mirrored = True
        for i in range(len(grid)):
            if grid[i][j] != grid[i][j+1]:
                mirrored = False
                break
        if mirrored:
            return j+1 + start
    return 0
    
    
def find_horizontal_mirroring(grid, start):
    grid = grid[start:]
    for i in range(len(grid)-1):
        if grid[i] == grid [i+1]:
            return i+1 + start
    return 0

def is_vertical_mirroring(grid, start):
    g1 = list(map(lambda x: x[:start], grid))
    g2 = list(map(lambda x: x[start:], grid))
    leng = min(len(g1[0]), len(g2[0]))
    for j in range(leng):
        for i in range(len(grid)):
            if g1[i][-j-1] != g2[i][j]:
                return False
    return True

def is_horizontal_mirroring(grid, start):
    g1 = grid[:start]
    g2 = grid[start:]
    leng = min(len(g1), len(g2))
    for i in range(leng):
            if g1[-i-1] != g2[i]:
                return False
    return True
        
        

def grid_print(grid):
    for l in grid:
        print(l)
    print()

#print(find_mirror_sums("example.txt"))
print(find_mirror_sums("input.txt"))


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0], l[-len(l)])