# optimal solution

def lengthOfLongestSubstring(s):
    hash_map = dict()
    left = 0
    right = 0
    length = 0
    n = len(s)
    while right < n:
        if s[right] in hash_map:
            left = max(hash_map[s[right]] + 1, left)
        hash_map[s[right]] = right
        length = max(length, right - left + 1)
        right += 1
    return length

# bruteforce by me

def longest_sunstring(s):
    maxi = 0
    box = set() 
    n = len(s)
    for i in range(n):
        substring_l = 0
        for j in range(i,n):
            if s[j] in box:
                maxi = max(maxi,substring_l)
                box.clear()
                break
            
            else:
                box.add(s[j])
                substring_l+=1
    return maxi

print(longest_sunstring("cadbzrsabdcd"))



# sir ka brute force

def lengthOfLongestSubstring( s):
    if len(s) == 0:
        return 0
    maxans = 0
    for i in range(len(s)):
        set = {}
        for j in range(i, len(s)):
            if s[j] in set:
                break
            maxans = max(maxans, j - i + 1)
            set[s[j]] = 1
    return maxans


print(lengthOfLongestSubstring("cadbdcd"))