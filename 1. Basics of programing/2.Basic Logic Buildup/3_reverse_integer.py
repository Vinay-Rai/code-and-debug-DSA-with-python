def reverse(x):   
    num = x
    n = abs(x)  # Use the absolute value of x to reverse
    reversed_num = 0

    while n > 0:
        last_digit = n % 10  # Get the last digit of n
        reversed_num = reversed_num * 10 + last_digit  # Append the last digit to reversed_num
        n = n // 10  # Remove the last digit from n

    if num < 0:
        reversed_num = -reversed_num  # Make the reversed number negative if the original was negative

    # Handling overflow: Check if the reversed number is within the 32-bit signed integer range
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0

    return reversed_num

print(reverse(1234))