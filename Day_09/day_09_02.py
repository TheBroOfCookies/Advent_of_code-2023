def extrapolates(filename): #solution: 1124
    extrapolated_sum = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            nums = list(map(lambda x: int(x), line.split()))
            extrapolated_sum += nums[0]
            diffs = find_diffs(nums)
            next_steps = []
            while not is_all_zeroes(diffs):
                next_steps.append(diffs[0])
                diffs = find_diffs(diffs)
            extrapolated_sum -= find_next_step(next_steps)
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

def find_next_step(steps):
    next_step = 0
    for step in steps[::-1]:
        next_step = step - next_step
    return next_step
            
            
#print(extrapolates("example.txt"))
print(extrapolates("input.txt"))