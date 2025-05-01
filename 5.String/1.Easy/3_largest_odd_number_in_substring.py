def largest_odd_number(sting):
    s = sting
    lst = list(s)
    print(lst)
    i = len(lst) -1
    index = -1
    while i>=0:
        if int(lst[i]) % 2 !=0:
            index = i
            break
        i-=1
    if index == -1:
        return ""
    else:
        return "".join(lst[:index+1])
    

print(largest_odd_number(""))



# sir ka easy hai because string iterable hai
def odd(num):
    num = "6743942474680"
    n = len(num)
    for i in range(n-1,-1,-1):  #tc = 0(n-k)
        if int(num[i]%2 == 1):
            return num[0:i+1]  #tc = 0(k)
    return ""

# total tc = 0(n)