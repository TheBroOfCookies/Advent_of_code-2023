def extrapolates(filename): #solution: 1921197370
    extrapolated_sum = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            nums = list(map(lambda x: int(x), line.split()))
            extrapolated_sum += nums[-1]
            diffs = find_diffs(nums)
            while not is_all_zeroes(diffs):
                extrapolated_sum += diffs[-1]
                diffs = find_diffs(diffs)
        return extrapolated_sum
                
            
def find_diffs(numbers):
    diffs = []
    for i in range(len(numbers)-1):
        diffs.append(numbers[i+1] - numbers[i])
    return diffs

def is_all_zeroes(nums):
    for n in nums:
        if n != 0:
            return False
    return True
            
            
#print(extrapolates("example.txt"))
print(extrapolates("input.txt"))