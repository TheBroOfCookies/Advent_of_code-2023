def find_lowest_location(filename):
    with open(filename) as file:
        lines = file.readlines()
        current_attrib = list(map(lambda x: int(x), lines[0].split(":")[1].split()))
        actual_start = 0
        for i in range(0, len(current_attrib), 2):
            actual_start += current_attrib[i+1]
        return actual_start
 
#print(find_lowest_location("example.txt"))
print(find_lowest_location("input.txt"))

#number of seeds found 2.207.992.808