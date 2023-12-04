def find_card_values(filename):
    with open(filename) as file:
        total_value = 0
        lines = file.readlines()
        for line in lines:
            line = line[:-1]
            line = line.split(":")[1]
            line = line.split("|")
            print(line)
            card_value = 0
            winning, actual = line[0].split(" "), line[1].split(" ")
            print(winning, actual)
            for win_num in winning:
                if win_num in actual and win_num != "":
                    if card_value == 0:
                        card_value = 1
                    else:
                        card_value *= 2
            total_value += card_value
    return total_value

print(find_card_values("input.txt"))