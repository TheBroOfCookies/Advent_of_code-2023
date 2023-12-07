card_to_sortable = {"2":"a", "3":"b", "4":"c", "5":"d", "6":"e", "7":"f", "8":"g", "9":"h", "T":"i", "J":"j", "Q":"k", "K":"l", "A":"m"} #solution: 253603890

class HandObj:
    def __init__(self, hand, bid, type, sortable):
        self.hand = hand
        self.bid = bid
        self.type = type
        self.sortable = sortable
    
    def __str__(self):
        return f"Hand: {self.hand}, Bid: {self.bid}, Type: {self.type}"

def find_total_winnings(filename):
    with open(filename) as file:
        lines = file.readlines()
        hands_ordered = [] #hand, bid, type
        for line in lines:
            hand, bid = line.strip().split()
            type = find_type_from_hand(hand)
            sortable = hand_to_sortable(hand)
            hands_ordered.append(HandObj(hand, int(bid), type, sortable))
            
        hands_ordered = sorted(hands_ordered, key=lambda x:x.sortable)
        hands_ordered = sorted(hands_ordered, key=lambda x:x.type)
        for hand in hands_ordered:
            print(hand, end =" ")
        print()
            
        sum_of_hands = 0
        for i in range(len(hands_ordered)):
            sum_of_hands += hands_ordered[i].bid * (i+1)
        return sum_of_hands
            
def find_type_from_hand(hand):
    count = [[hand[0], 1], [hand[1], 1], [hand[2], 1], [hand[3], 1], [hand[4], 1]]
    for i in range(len(hand)):
        if hand[i] == count[0][0] and i > 0:
            count[0][1] += 1
        elif hand[i] == count[1][0] and i > 1:
            count[1][1] += 1
        elif hand[i] == count[2][0] and i > 2:
            count[2][1] += 1
        elif hand[i] == count[3][0] and i > 3:
            count[3][1] += 1

    count = sorted(count, key=lambda x: x[1])

    if count[4][1] == 5:                        #6: five of a kind
        return 6
    elif count[4][1] == 4:                      #5: four of a kind
        return 5
    elif count[4][1] == 3 and count[3][1] == 2: #4: full house
        return 4
    elif count[4][1] == 3:                      #3: three of a kind
        return 3
    elif count[4][1] == 2 and count[3][1] == 2: #2: two pair
        return 2
    elif count[4][1] == 2:                      #1: one pair
        return 1
    else:                                       #0: high card
        return 0
    
def hand_to_sortable(hand):
    sortable = ""
    for card in hand:
        sortable += card_to_sortable[card]
    return sortable

print(find_total_winnings("input.txt"))