def find_mirror_sums(filename):  #solution: 28806
    with open(filename) as file:
        lines = file.readlines()
        sum = 0
        accum = []
        for line in lines:
            if line == "\n" or line == "":
                grid_print(accum)
                hort = 0
                for h in range(1,len(accum)):
                    if is_horizontal_mirroring(accum, h):
                        hort = h
                        break
                vert = 0
                if hort == 0:
                    for v in range(1,len(accum[0])):
                        if is_vertical_mirroring(accum, v):
                            vert = v
                            break
                sum += vert + hort*100
                accum = []
                
            else:
                accum.append(line.strip())
                
        return sum

def is_vertical_mirroring(grid, start):
    g1 = list(map(lambda x: x[:start], grid))
    g2 = list(map(lambda x: x[start:], grid))
    leng = min(len(g1[0]), len(g2[0]))
    smudge = 0
    for j in range(leng):
        for i in range(len(grid)):
            if g1[i][-j-1] != g2[i][j]:
                if smudge == 0:
                    smudge = 1
                else:
                    return False
    return smudge

def is_horizontal_mirroring(grid, start):
    g1 = grid[:start]
    g2 = grid[start:]
    leng = min(len(g1), len(g2))
    smudge = 0
    for i in range(leng):
        if g1[-i-1] != g2[i]:
            if smudge == 0:
                for j in range(len(g1[-i-1])):
                    if g1[-i-1][j] != g2[i][j]:
                        if smudge == 0:
                            smudge = 1
                        else:
                            return False
            else:
                return False
    return smudge
        
def grid_print(grid):
    for l in grid:
        print(l)
    print()

#print(find_mirror_sums("example.txt"))
print(find_mirror_sums("input.txt"))
