def prints(count):
    if count==0:
        return
    print("vinay")
    prints(count-1)

prints(4)


#prints x n times
def func(x,n):
    if n == 0:
        return
    print(x)
    func(x,n-1)

#prints 1 to n
def oneton(n):
    if n == 0:
        return
    oneton(n-1)
    print(n)


#prints 1 to n
def func1(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)