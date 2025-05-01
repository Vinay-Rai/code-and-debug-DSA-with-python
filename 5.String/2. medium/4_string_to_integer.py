def string_to_int(s):
    result = ""
    sc = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"."}
    
    si  = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    ss = {"+","-"}

    for i in range(len(s)):
        if s[0] in sc:
            return result
        elif s[i] in ss and result=="":
            result+=s[i]
        elif s[i] in ss:
            return result
        elif s[i] in si:
            result+=s[i]
        print(result)
    return result


print(string_to_int(" -042"))
    