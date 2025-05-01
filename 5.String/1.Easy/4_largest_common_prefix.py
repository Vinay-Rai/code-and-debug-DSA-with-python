# Python program to find the longest common prefix
# using Sorting

def longestCommonPrefix(strs):

    strs.sort()
    first = strs[0]
    last = strs[-1]
    minLength = min(len(first), len(last))
    if minLength == 0:
        return ""

    i = 0
    while i < minLength and first[i] == last[i]:
        i += 1

    return first[:i]



# sir wala
def commom_prefix(strs):
    if len(strs) == 0:
        return  ""
    result = ""
    base = strs[0]
    for i in range(0,len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i]!=base[i]:
                return result
        result += base[i]
    return result

print(commom_prefix(["flower","flowr","flight"]))

# tc = 0(m*n)
# sc = 0(1)  or 0(n)