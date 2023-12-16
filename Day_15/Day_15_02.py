def find_hash_sum(filename):  #solution: 231844
    with open(filename) as file:
        line = file.read()
        line = line.split(",")
        boxes =[[] for i in range(256)]
        for seq in line:
            if "=" in seq:
                seq = seq.split("=")
                hash = get_hash(seq[0])
                seq[1] = int(seq[1])
                i = check_for_lens(seq[0], boxes[hash])
                if i != -1:
                    boxes[hash][i][1] = seq[1] #replace
                else:
                    boxes[hash].append(seq) #append
            else:
                seq = seq[:-1]
                hash = get_hash(seq)
                i = check_for_lens(seq, boxes[hash])
                if i > -1:
                    boxes[hash].pop(i)
        boxes_print(boxes)
        return find_box_sum(boxes)

def get_hash(seq):
    hash = 0
    for ch in seq:
        hash = ((hash+ord(ch)) * 17) % 256
    return hash

def check_for_lens(lense_name, box):
    for i in range(len(box)):
        if box[i][0] == lense_name:
            return i
    return -1

def boxes_print(boxes):
    for i in range(len(boxes)):
        if len(boxes[i]) > 0:
            print(i, boxes[i])
            
def find_box_sum(boxes):
    sum = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            sum += (i+1) * (j+1) * boxes[i][j][1]
    return sum

#print(find_hash_sum("example.txt")) # solution: 5139
print(find_hash_sum("input.txt"))