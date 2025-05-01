n = 1234
num = n  #esa isliye kiya ki hamara input change na ho jaye
count = 0

#is code me humne no = 0  and negative number wala case handle nahi kiya
while num > 0:
    last_digit = num % 10
    print(last_digit)
    count+=1
    num = num // 10
print(count)


#another method using log
from math import *
def count_digits(num):
    if num==0:         #special case for zero
        return 1
    return int(log10(abs(num))+1) #abs value to handle negative no.

print(count_digits(n))