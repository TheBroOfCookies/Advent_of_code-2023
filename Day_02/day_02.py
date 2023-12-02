#example = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
#output = 2727
def find_legal_games(filename):
    with open(filename) as file:
        legal_games = 0
        lines = file.readlines()
        for line in lines:
            game, line = split_line(line)
            legal_games += check_line(line, game)
    return legal_games

def split_line(line):
    line = line.split(":")
    game, line = line[0], line[1]
    game = int(game.split(" ")[1])
    line = line.split(";")
    for i in range(len(line)):
        if "," in line[i]:
            processed = line[i].split(",")
            line[i] = processed[0]
            line += processed[1:]
                
    line = list(map(lambda x: x.split(), line))
    return game, line

def check_line(line, game):
    balls_max = {"red": 12, "green": 13, "blue": 14}
    for occur in line:
        color, num = occur[1], int(occur[0])
        if num > balls_max[color]:
            return 0
    return game


print(find_legal_games("input.txt"))