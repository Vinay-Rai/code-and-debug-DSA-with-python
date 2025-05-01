def convert2binary(num):
    result = ""
    while num > 0:
        if num % 2 ==1:
            result ="1" +result
        else:
            result= "0" + result
        num = num//2
    return result

print(convert2binary(13))