def find_part_sum(filename):
    legal_symbols = ['*', '/', '%', '+', '$', '=', '&', '#', '@', '-']
    part_sum = 0
    with open(filename) as file:
        lines = file.readlines()
        
        for i in range(1, len(lines)-1): #no symbols in frist and last line
            for j in range(len(lines[i])):
                sym = lines[i][j]
                if sym in legal_symbols:
                    part_sum += partial_sum_from_seed(j, [lines[i-1], lines[i], lines[i+1]])
                    
    return part_sum

def partial_sum_from_seed(seed, line_to_check):
    partial_sum = 0
    for line in line_to_check:
        for y in [-1, 0, 1]:
            if seed+y < 0 or seed+y >= len(line): #index out of bound protection
                continue
            if line[seed+y].isnumeric():
                number, right_append = grow_number(seed+y, line)
                partial_sum += number
                if y != 1 and right_append: #avoid adding duplicate numbers
                    break
            
    return partial_sum
           
    
def grow_number(start, line):
    number_buff = [line[start]]
    right_append = False
    #check numebr growing to the left
    if line[start-1].isnumeric():
        number_buff.insert(0, line[start-1])
        if line[start-2].isnumeric():
            number_buff.insert(0, line[start-2])
    #check number grwoth to the right
    if line[start+1].isnumeric():
        number_buff.append(line[start+1])
        right_append = True
        if line[start+2].isnumeric():
            number_buff.append(line[start+2])
    return int("".join(number_buff)), right_append
        
print(find_part_sum("input.txt"))
