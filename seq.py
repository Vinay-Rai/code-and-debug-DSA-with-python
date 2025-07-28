import sys

def GetAnswer(N, M, S, T):
    prefix = [-1] * M
    suffix = [-1] * M

    # Step 1: Match T from left to right in S (prefix)
    j = 0
    for i in range(N):
        if j < M and S[i] == T[j]:
            prefix[j] = i
            j += 1

    # T is not a subsequence of S
    if j < M:
        return 0

    # Step 2: Match T from right to left in S (suffix)
    j = M - 1
    for i in reversed(range(N)):
        if j >= 0 and S[i] == T[j]:
            suffix[j] = i
            j -= 1

    # T is not a subsequence of S
    if j >= 0:
        return 0

    # Step 3: Find maximum gap between prefix[i] and suffix[i+1]
    max_gap = 0
    for i in range(M - 1):
        max_gap = max(max_gap, suffix[i + 1] - prefix[i] - 1)

    # Final answer is length of T + max_gap
    return max_gap + M



# Output
print(GetAnswer(10,3,"abcacdjklh","acd"))

