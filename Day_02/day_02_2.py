from functools import reduce
#example = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
#output 56580

def find_power_sum(filename):
    with open(filename) as file:
        lines = file.readlines()
        return sum(count_line(split_line(line)) for line in lines)

def split_line(line):
    line = line.split(":")[1]
    line = line.split(";")
    for i in range(len(line)):
        if "," in line[i]:
            processed = line[i].split(",")
            line[i] = processed[0]
            line += processed[1:]
                
    line = list(map(lambda x: x.split(), line))
    return line

def count_line(line):
    balls_min = {"red": 0, "green": 0, "blue": 0}
    for occur in line:
        color, number_of_balls = occur[1], int(occur[0])
        balls_min[color] = max(balls_min[color], number_of_balls)
    return reduce(lambda x, y: x*y, balls_min.values())

print(find_power_sum("input.txt"))