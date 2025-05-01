def factors(num):
    s=[]

    for i in range(1,num//2+1):
        if num % i == 0:
            s.append(i)
    s.append(num)
    return(s)

print(factors(11))


#to add in set s.add(i)


#OPTIMAL APPROACH

def factors_optimal(num):
    from math import sqrt
    result = []
    for i in range (1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if num//i !=i:
                result.append(num//i)
    return result

print(factors_optimal(12))