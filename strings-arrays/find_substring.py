#Not working solution
def Substr(Str, target):
     
    t = 0
    Len = len(Str)
    i = 0
     
    # Iterate from 0 to Len - 1
    for i in range(Len):
        if (t == len(target)):
            break
        if (Str[i] == target[t]):
            t += 1
        elif Str[i] == target[0]:
            t = 1
        else:
            t = 0
             
    if (t < len(target)):
        return -1
    else:
        return (i - t + 1)


print(Substr("Helloo", "lo"))
print(Substr("Helllloo", "loo"))