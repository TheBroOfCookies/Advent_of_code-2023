import numpy as np
from copy import deepcopy

RIGHT = np.array([0,1])
DOWN = np.array([1,0])
LEFT = np.array([0,-1])
UP = np.array([-1,0])

class Beam:
    def __init__ (self, coord, direction):
        self.coord = coord
        self.direction = direction

def find_energy_sum(filename):  #solution: 7041
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    #grid_print(grid)
    
    grid_dims = [len(grid), len(grid[0])]
    print("Dims:", grid_dims[0], grid_dims[1])
    print("Max beams:",grid_dims[0]*grid_dims[1]*4)
    
    best_sum = -1
    for i in range(grid_dims[0]):
        grid_nrg = move_beams([Beam(np.array([i,-1]), RIGHT)], grid)
        best_sum = max(np.sum(grid_nrg), best_sum)
    for i in range(grid_dims[0]):
        grid_nrg = move_beams([Beam(np.array([i, grid_dims[1]]), LEFT)], grid)
        best_sum = max(np.sum(grid_nrg), best_sum)
        
    for j in range(grid_dims[1]):
        grid_nrg = move_beams([Beam(np.array([-1,j]), DOWN)], grid)
        best_sum = max(np.sum(grid_nrg), best_sum)
    for j in range(grid_dims[1]):
        grid_nrg = move_beams([Beam(np.array([grid_dims[0],j]), UP)], grid)
        best_sum = max(np.sum(grid_nrg), best_sum)
    
    #grid_nrg_print(grid_nrg)
    return best_sum

def move_beams(beams, grid):
    grid_dims = [len(grid), len(grid[0])]
    grid_nrg = np.zeros(grid_dims, dtype=int)
    grid_history = deepcopy(grid)
    for i in range(grid_dims[0]):
        for j in range(grid_dims[1]):
            grid_history[i][j] = np.array([], dtype=int)
    out_of_bounds = 0
    looped = 0

    while len(beams):
        beam = beams[0]
        beam.coord += beam.direction
        i, j = beam.coord
        
        if i < 0 or i >= grid_dims[0] or j < 0 or j >= grid_dims[1]:
            beams.pop(0)
            out_of_bounds += 1
            continue
        
        elif is_in_history(grid_history[i][j], beam.direction):
            beams.pop(0)
            looped += 1
            continue
        
        grid_nrg[i][j] = 1
        grid_history[i][j] = [beam.direction]
    
        sym = grid[i][j]
        if sym == "\\" or sym == "/":
            beam.direction = dir_change(beam.direction, sym)
        elif sym == "|":
            if should_split(beam.direction, sym):
                beams.append(Beam(np.copy(beam.coord), UP))
                beam.direction = DOWN
        elif sym == "-":
            if should_split(beam.direction, sym):
                beams.append(Beam(np.copy(beam.coord), LEFT))
                beam.direction = RIGHT
    
    print("Total beams:", out_of_bounds + looped, "  Out of bound:", out_of_bounds, "  Looped:", looped)
    return grid_nrg
                
            
def dir_change(direction, symbol):
    if symbol == "\\":
        if np.array_equal(direction, RIGHT):
            return DOWN
        elif np.array_equal(direction, DOWN):
            return RIGHT
        elif np.array_equal(direction, LEFT):
            return UP
        elif np.array_equal(direction, UP):
            return LEFT
    if symbol == "/":
        if np.array_equal(direction, RIGHT):
            return UP
        elif np.array_equal(direction, DOWN):
            return LEFT
        elif np.array_equal(direction, LEFT):
            return DOWN
        elif np.array_equal(direction, UP):
            return RIGHT
    
def should_split(direction, sym):
    if sym == "-":
        return np.array_equal(direction, UP) or np.array_equal(direction, DOWN)
    elif sym == "|":
        return np.array_equal(direction, LEFT) or np.array_equal(direction, RIGHT)
    
def is_in_history(tile_history, direction):
    for dir in tile_history:
        if np.array_equal(dir, direction):
            return True
    return False
    
    
def grid_print(grid):
    for l in grid:
        for s in l:
            print(s,end="")
        print()
    print()
    
def grid_nrg_print(grid):
    for l in grid:
        for s in l:
            if s == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()
    print()

def grid_history_print(grid):
    for l in grid:
        for s in l:
            print(len(s),end="")
        print()
    print()
    
#print(find_energy_sum("example.txt"))
print(find_energy_sum("input.txt"))