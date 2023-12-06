races = [[53, 333], [83, 1634], [72, 1289], [88, 1532]] #solution 140200
result = 1
for time, dist in races:
    result *= sum(1 if i*(time-i) > dist else 0 for i in range(time))

print(result)