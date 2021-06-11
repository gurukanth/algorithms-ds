def grid_traveller(m:int, n:int, memo:dict={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        memo[key] = grid_traveller(m-1, n, memo) + grid_traveller(m, n-1, memo)
        return memo[key]


print(grid_traveller(2, 3))
print(grid_traveller(3, 3))
print(grid_traveller(4, 4))
print(grid_traveller(5, 5))
print(grid_traveller(10, 10))
print(grid_traveller(15, 15))