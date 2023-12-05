def find_lowest_location(filename):
    attributes = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    attrib_index = 0

    with open(filename) as file:
        lines = file.readlines()
        current_attrib = list(map(lambda x: int(x), lines[0].split(":")[1].split()))
        next_attrib = []
        #print(current_attrib)
        
        for line in lines[1:]:
            if  "map" in line:
                for val in current_attrib:
                    next_attrib.append(val)
                current_attrib = next_attrib
                next_attrib = []
                print(attributes[attrib_index])
                print(current_attrib)
                attrib_index += 1
                continue
            if len(line) < 2:
                continue
            
            line = line.strip().split(" ")
            dest, source, span = int(line[0]), int(line[1]), int(line[2])
            #print(dest, source, span)
            current_attrib_copy = current_attrib.copy()
            for val in current_attrib:
                #print(source + span)
                if val >= source and val < (source + span):
                    #print(val)
                    #print("Val: ", val, "  Steps: ", val - source, "  Dest: ", dest, "  Map dest: ",  dest+(val - source) ," \t",dest, source, span)
                    next_attrib.append(dest+(val - source))
                    current_attrib_copy.remove(val)
            current_attrib = current_attrib_copy
        for val in current_attrib:
                    next_attrib.append(val)
                    
        print(attributes[attrib_index])
        print(next_attrib)
        return min(next_attrib)
 


print(find_lowest_location("input.txt"))
#print(find_lowest_location("input.txt"))

"""
seed_to_soil

soil-to-fertilizer

fertilizer-to-water

water-to-light

light-to-temperature

temperature-to-humidity

humidity-to-location
"""