counter:int = 1
def power(base, exponent):
    global counter
    counter += 1
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return power(base * base, exponent/2)
    else:
        return base * power(base * base, (exponent-1)/2)

print(power(7,1200))
print('---------------')
print(counter)
