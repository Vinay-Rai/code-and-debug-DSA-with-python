def palindrome(num):
    n = num
    reverse_num = 0
    
    #negative number and 0 wala case handle nahi ho raha hai
    while num > 0:
        remainder = num % 10
        reverse_num = reverse_num*10 + remainder
        num = num // 10
    
    return reverse_num == n

print(palindrome(1223221))