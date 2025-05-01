def armstrong(num):
    n = num
    lth = len(str(n))
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result + last_digit**lth
        num  = num//10
    
    return n == result

print(armstrong(1634))