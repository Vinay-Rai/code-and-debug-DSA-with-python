def convert2decimal(x):
    decimal_number = 0
    power = 0
    index = len(x) -1
    while index >=0:
        num = int(x[index])*(2**power)
        decimal_number+=num
        index-=1
        power+=1
    return decimal_number

print(convert2decimal("1111"))
print(bin(15))