def find_longest_path(filename): #solution: 2130
    print("Reading from file...")
    grid = []
    with open(filename) as file:
        for line in file.readlines():
            line = list(line.strip())
            grid.append(line)
            
    n,m = len(grid), len(grid[0])
    start = 1
    #grid_print(grid)
    print("Generating edges...")
    edges, dist, pred = generate_edges(grid,n,m)
    dist[start] = 0
    #print(edges)
    print("Updating edges...")
    edges = get_new_edges_BFS(edges,n,m)
    #for e in edges.values():
    #    if len(e) > 1:
    #        print(e)
    #print(edges)
    print("Finding longest path...")
    dist = bellman_ford(edges, dist, pred)
    return dist[(n*m)-2]*-1

def bellman_ford(edges, dist, pred):
    for r in range(len(edges.keys())-1):
        for v in edges.keys():
            for u in edges[v]:
                dv = dist[v]
                du = dist[u]
                if dv-1 < du:
                    dist[u] = dv-1
                    pred[u] = v
    return dist

                    
def get_new_edges_BFS(edges,n,m):
    prev = 1
    q = [(1, 0)]
    visited = [1]
    while len(q):
        #print(q)
        c, prev = q.pop(0)
        #print(f"{c}:{index_to_symbol(c,m)}", edges[c])
        edg = edges[c].copy()
        for e in edg:
            if e == prev:
                edges[c].remove(e)
                continue
            if not e in visited:
                q.append((e, c))
                visited.append(e)
    return edges


def generate_edges(grid, n, m):
    edges = {}
    dist = {}
    pred = {}
    dirs=((0,1), (1,0), (0,-1), (-1,0))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            index = i*n+j
            edges[index]  = []
            dist[index]  = 1000
            pred[index]  = None
            for off_i, off_j in dirs:
                ii = i + off_i
                jj = j + off_j
                if ii not in range(n) or jj not in range(m):
                    continue
                symbol = grid[ii][jj]
                to_add = False
                if symbol == ".":
                    to_add = True
                elif symbol != "#":
                    if symbol == "<" and jj < j:
                        to_add = True
                    elif symbol == ">" and jj > j:
                        to_add = True
                    elif symbol == "^" and ii < i:
                        to_add = True
                    elif symbol == "v" and ii > i:
                        to_add = True
                if to_add:
                    """
                    if symbol != "#":
                    """
                    edges[index].append((ii*n+jj))
    return edges, dist, pred
       
def grid_print(grid):
    for l in grid:
        for s in l:
            print(s, end="") 
        print()
    print()


#print(find_longest_path("example.txt")) #expected: 94
print("Longest path:",find_longest_path("input.txt"))
