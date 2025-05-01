def XORfrom1ToN( num):
    if num % 4 == 1:
        return 1
    elif num % 4 == 2:
        return num + 1
    elif num % 4 == 3:
        return 0
    else:
        return num

def findXOR( l, r):
    return XORfrom1ToN(l - 1) ^ XORfrom1ToN(r)

print(findXOR(5,7))