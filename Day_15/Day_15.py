def find_hash_sum(filename):  #solution: 516804
    with open(filename) as file:
        line = file.read()
        line = line.split(",")
        hash_sum = sum(map(lambda x: get_hash(x), line))    
        return hash_sum 

def get_hash(seq):
    hash = 0
    for ch in seq:
        hash = ((hash+ord(ch)) * 17) % 256
    return hash

#print(find_hash_sum("example.txt"))
print(find_hash_sum("input.txt"))