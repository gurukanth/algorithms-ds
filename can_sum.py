
def can_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for number in numbers:
        remainder = target_sum - number
        if can_sum(remainder, numbers, memo) == True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False



print(can_sum(7, [1, 2, 3, 4])) # true
print(can_sum(7, [2,4])) #false
print(can_sum(0, [1, 2])) # true
print(can_sum(8, [2,3,5])) # true
print(can_sum(1235, [5, 4, 3, 2]) )#true