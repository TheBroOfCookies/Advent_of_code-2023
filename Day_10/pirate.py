
from collections import deque

my_input = open(f"input.txt").read()

print("Step 1: Raw Input")
print(my_input)

print("\nStep 2: Expand Each Tile to a 3x3 Grid")

One2ThreeMAP = {"|": ".#..#..#.",
                "-": "...###...",
                "L": ".#..##...",
                "J": ".#.##....",
                "7": "...##..#.",
                "F": "....##.#.",
                ".": ".........",
                "S": "....#...."}

G_Original = []
for row, line in enumerate(my_input.strip().splitlines()):
    G_Original.append(line)
    if "S" in line:
        r_start, c_start = row, line.find("S")

G = [[" " for _ in range(len(G_Original[0]) * 3)] for _ in range(len(G_Original) * 3)]

for r in range(len(G_Original)):
    for c in range(len(G_Original[0])):
        for dr in range(3):
            for dc in range(3):
                G[r * 3 + dr][c * 3 + dc] = One2ThreeMAP[G_Original[r][c]][dr * 3 + dc]

print('\n'.join(''.join(row) for row in G))

r, c = r_start * 3 + 1, c_start * 3 + 1

print('\nStep 3: Connect S to the corresponding endings')

if G[r + 2][c] == "#":
    G[r + 1][c] = "#"
if G[r - 2][c] == "#":
    G[r - 1][c] = "#"
if G[r][c + 2] == "#":
    G[r][c + 1] = "#"
if G[r][c - 2] == "#":
    G[r][c - 1] = "#"

print('\n'.join(''.join(row) for row in G))

print('\nPart 1: Follow the pipe, count the number of elements, and divide the total by both 3 and 2')

Q = deque()
Q.append((r, c))
seen = set()

while Q:
    r, c = Q.popleft()

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(G) and 0 <= cc < len(G[0]) and (rr, cc) not in seen and G[rr][cc] == "#":
            Q.append((rr, cc))
            seen.add((rr, cc))

print("Solution part 1:", len(seen) // 3 // 2)

print(
    '\nPart 2: Remove the tiles not on the path and flood-fill the grid, starting at (0,0) and count tiles with 3x3 dots')

for r in range(len(G)):
    for c in range(len(G[0])):
        if (r, c) not in seen:
            G[r][c] = "."

Q = deque()
Q.append((0, 0))
seen = set()

while Q:
    r, c = Q.popleft()
    G[r][c] = " "

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(G) and 0 <= cc < len(G[0]) and (rr, cc) not in seen and G[rr][cc] == ".":
            Q.append((rr, cc))
            seen.add((rr, cc))

print('\n'.join(''.join(row) for row in G))

p2 = 0
for r in range(len(G_Original)):
    for c in range(len(G_Original[0])):
        p2 += 1 if all(G[r * 3 + dr][c * 3 + dc] == "." for dr in range(3) for dc in range(3)) else 0

print("Solution part 2:", p2)


# OUTPUT
# Step 1: Raw Input
# ..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# ..........
#
# Step 2: Expand Each Tile to a 3x3 Grid
# ..............................
# ....#.####################....
# .........................#....
# ....#....................#....
# ....#..################..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#######..#######..#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....##########..##########....
# ..............................
#
# Step 3: Connect S to the corresponding endings
# ..............................
# ....######################....
# ....#....................#....
# ....#....................#....
# ....#..################..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#..............#..#....
# ....#..#######..#######..#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....#........#..#........#....
# ....##########..##########....
# ..............................
#
# Part 1: Follow the pipe, count the number of elements, and divide the total by both 3 and 2
# Solution part 1: 22
#
# Part 2: Remove the tiles not on the path and flood-fill the grid, starting at (0,0) and count tiles with 3x3 dots
#
#     ######################
#     #....................#
#     #....................#
#     #..################..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#              #..#
#     #..#######  #######..#
#     #........#  #........#
#     #........#  #........#
#     #........#  #........#
#     #........#  #........#
#     #........#  #........#
#     ##########  ##########
#
# Solution part 2: 4
