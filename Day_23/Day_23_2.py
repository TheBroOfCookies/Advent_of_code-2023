from copy import deepcopy

def find_longest_path(filename): #solution: 6710
    print("Reading from file...")
    grid = []
    with open(filename) as file:
        for line in file.readlines():
            line = list(line.strip())
            grid.append(line)
            
    n,m = len(grid), len(grid[0])
    print("Generating edges...")
    edges, dist = generate_edges(grid,n,m)
    print("Updating edges...")
    edges = get_new_edges(edges)
    edges = shorten_edges(grid, edges,m)
    edges = mirror_edges(edges,m)
    print("Finding longest path...")
    print("Note: This may take a few minutes, so please be patient")
    dist = longest_DFS(edges, m, (1,0))
    return dist


def longest_DFS(edges, m, start, dist=0, visited=[]):
    end = (m**2)-2
    q = [start]
    best = 0
    total_dist = dist
    while len(q):
        c, w = q.pop()
        if c in visited:
            continue
        visited.append(c)
        total_dist += w
        if c == end:
            return max(best, total_dist)
        edg = edges[c]
        q.append(edg[0])
        for e in edg[1:]:
            if e in visited:
                continue
            v = visited.copy()
            best = max(best, longest_DFS(edges, m, e, total_dist, v))
    return best

def mirror_edges(edges,m):
    new_edges = deepcopy(edges)
    for k in edges.keys():
        for v,w in edges[k]:
            if v == m**2-2 or k == 1:
                continue
            k_found = False
            for check_k,ww in edges[v]:
                if k == check_k:
                    k_found = True
                    break
            if not k_found:
                new_edges[v].append((k,w))
    for k in new_edges.keys():
        for v,w in new_edges[k]:
            if v == (m**2)-2:
                new_edges[k] = [(v,w)]
                return new_edges
                

def shorten_edges(grid,edges,m):
    new_edges = {}
    end = (m**2)-2
    q = [(1, 0, 1)] #node, dist, prev_ckeck
    while len(q):
        c, dist, prev_check = q.pop()
        if c == end:
            if prev_check in new_edges.keys():
                if not (c,dist) in new_edges[prev_check]:
                    new_edges[prev_check].append((c, dist))
            else:
                new_edges[prev_check] = [(c, dist)]
        dist += 1
        i,j = c//m, c%m
        edg = edges[c]
        if not len(edg):
            continue
        if grid[i][j] == ".":
            q.append((edg[0], dist, prev_check))
            continue
        c = edg[0]
        dist += 1
        if prev_check in new_edges.keys():
            if not (c,dist) in new_edges[prev_check]:
                new_edges[prev_check].append((c, dist))
        else:
            new_edges[prev_check] = [(c, dist)]
        for e in edges[c]:
            ed = edges[e][0]
            q.append((ed, 1, c))
    return new_edges

def get_new_edges(edges):
    prev = 1
    q = [(1, 0)]
    visited = [1]
    while len(q):
        c, prev = q.pop(0)
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
    dirs=((0,1), (1,0), (0,-1), (-1,0))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            index = i*n+j
            edges[index]  = []
            dist[index]  = 1000
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
                    edges[index].append((ii*n+jj))
    return edges, dist
       
def grid_print(grid):
    for l in grid:
        for s in l:
            print(s, end="") 
        print()
    print()
    


#print(find_longest_path("example.txt")) #expected: 154
print("Longest path:",find_longest_path("input.txt"))
