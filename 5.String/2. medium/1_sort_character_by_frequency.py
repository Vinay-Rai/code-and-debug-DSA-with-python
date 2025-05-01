def sort_character_by_frequency(s):
    result = ""
    hash_map = {}
    for ch in s:
        hash_map[ch] = hash_map.get(ch,0)+1

    sorted_char = sorted(hash_map.items(),key = lambda x:x[1],reverse=True)
    for ch,freq in sorted_char:
        result = result + (ch*freq)
    return result

print(sort_character_by_frequency("tree"))