def find_card_values(filename):
    with open(filename) as file:
        lines = file.readlines()
        total_cards = [1]*(len(lines))
        print(len(total_cards))
        for i in range(len(lines)):
            line = lines[i]
            line = line[:-1]
            line = line.split(":")[1]
            line = line.split("|")
            print(i)
            print(total_cards)
            card_value = 0
            winning, actual = line[0].split(" "), line[1].split(" ")
            #print(winning, actual)
            for win_num in winning:
                if win_num in actual and win_num != "":
                        card_value += 1
            if card_value > 0:
                cards = total_cards[i]
                for j in range(1, card_value+1):
                    try:
                        total_cards[i+j] += cards
                    except:
                        pass
                    
            
    return sum(total_cards)

print(find_card_values("input.txt"))