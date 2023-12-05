def find_lowest_location(filename):
    attributes = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    attrib_index = 0

    with open(filename) as file:
        lines = file.readlines()
        current_attrib = list(map(lambda x: int(x), lines[0].split(":")[1].split()))
        actual_start = []
        for i in range(0, len(current_attrib), 2):
            actual_start.append([current_attrib[i], current_attrib[i+1]])
        current_attrib = actual_start
        next_attrib = []
        print(current_attrib)
        
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
            current_attrib_copy = current_attrib.copy()
            for val, leng in current_attrib:
                if(val+leng <= source or val >= source+span): #case 5 or 6
                    continue
                if val >= source: #case 1, 2
                    if (leng <= span): #case 1
                        next_attrib.append([dest+(val - source), leng])
                        current_attrib_copy.remove([val, leng])
                    else:  #case 2 (val+len > source + span)
                        next_attrib.append([dest+(val - source), span-(val-source)])
                        current_attrib_copy.remove([val, leng])
                        current_attrib_copy.append([source+span, leng+(val-source)-span])
                else: # case 3 or 4 (val < source and val+leng > source)
                    if (val+leng < source+span): #case 3
                        next_attrib.append([dest, leng-(source-val)])
                        current_attrib_copy.remove([val, leng])
                        current_attrib_copy.append([val, source-val])
                    #else: #case 4 (Case 4 never occurs)
                    #    next_attrib.append([dest, span])
                    #    current_attrib_copy.remove([val, leng])
                    #    current_attrib_copy.append([val, source-val])
                    #    current_attrib_copy.append([source+span, leng-span-(source-val)])
                #else case 5 or 6, do nothing
                    
            current_attrib = current_attrib_copy
        for val in current_attrib:
                    next_attrib.append(val)
                    
        print(attributes[attrib_index])
        print(next_attrib)
        return min(next_attrib)
 
#print(find_lowest_location("example.txt"))
print(find_lowest_location("input.txt"))
