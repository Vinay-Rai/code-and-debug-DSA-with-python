def rotate_string(s,goal):
    newstring = ""
    n=len(s)
    for i in range(n):
        newstring = s[n-i:] + s[:n-i] 
        print(newstring)
        if newstring == goal:
            return True
    return False


s= "abcde"
goal = "cdeab"
print(rotate_string(s,goal))