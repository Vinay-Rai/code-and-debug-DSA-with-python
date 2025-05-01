def anagram(s,t):
    if len(s)!=len(t):
        return False
    freq_s = {}
    freq_t = {}
    for i in s:
        if i not in freq_s:
            freq_s[i] = 1
        else:
            freq_s[i]+=1

    for i in t:
        if i not in freq_t:
            freq_t[i] = 1
        else:
            freq_t[i]+=1

    for i in s:
        if i not in freq_t:
            return False
        if freq_s[i] != freq_t[i]:
            return False

    return True

print(anagram("anagram","bramnaa"))



# using sorting

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        return True
    return False