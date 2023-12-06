time, dist = [53837288, 333163512891532] #solution: 39570185    #time, dist = [71530, 940200] #solution: 71503
print(sum(1 if i*(time-i) > dist else 0 for i in range(time)))