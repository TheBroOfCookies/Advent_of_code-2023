import heapq

def minimal_heat_loss(filename):  #solution: 665
    grid = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(map(lambda x: int(x), list(line.strip()))))
            
    grid_dims = [len(grid), len(grid[0])]
    print("Dims", grid_dims, "Max paths", grid_dims[0]*grid_dims[1]**3)
    
    return move_max([(0, 0, 0, 0, -1)], grid)

def move_max(moves, grid):
    grid_dims = [len(grid), len(grid[0])]
    seen = set()
    while len(moves):
        loss, pos_x, pos_y, straights, prev_dir = heapq.heappop(moves)
            
        if pos_y == grid_dims[0]-1 and pos_x == grid_dims[1]-1:
            print("Reached end with", loss, "loss")
            return loss
        if (pos_x, pos_y, prev_dir, straights) in seen:
            continue
        seen.add((pos_x, pos_y, prev_dir, straights))

        for next_dir in range(4):
            if (next_dir + 2 % 4) == prev_dir:
                continue
            if next_dir == prev_dir and straights >= 3:
                continue
            next_x, next_y = offset_pos(pos_x, pos_y, next_dir)
            if next_y not in range(grid_dims[0]) or next_x not in range(grid_dims[1]):
                continue

            next_loss = loss + grid[next_y][next_x]
                
            if next_dir == prev_dir:
                heapq.heappush(moves, (next_loss, next_x, next_y, straights+1, next_dir))
            else:
                heapq.heappush(moves, (next_loss, next_x, next_y, 1, next_dir))



def offset_pos(pos_x, pos_y, move):
    if move == 0:
        return pos_x + 1, pos_y
    if move == 1:
        return pos_x, pos_y + 1
    if move == 2:
        return pos_x - 1, pos_y
    if move == 3:
        return pos_x, pos_y - 1

def grid_print(grid):
    for l in grid:
        for s in l:
            print(s,end="")
        print()
    print()
    
            
#print(minimal_heat_loss("example.txt"))
print(minimal_heat_loss("input.txt"))
