def minBitFlips(start, goal):
    ans = start ^ goal
    count = 0
    for i in range(0, 32):
        if ans & (1 << i) != 0:
            count += 1
    return count

print(minBitFlips(0,15))


# second method log(n) time complexity
def minBitFlips( start, goal):
    ans = start ^ goal
    count = 0
    while ans > 0:
        if ans % 2 == 1:
            count += 1
        ans = ans // 2
    return count