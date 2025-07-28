def solve():
    import sys
    input = sys.stdin.read
    from collections import defaultdict

    data = list(map(int, input().split()))
    N = data[0]
    A = data[1:]

    MOD = 10**9 + 7

    prefix_freq = defaultdict(int)
    suffix_freq = defaultdict(int)
    left_count = [0] * N
    right_count = [0] * N

    # Counting prefix frequencies (for frequency(i, i, A[i]))
    for i in range(N):
        prefix_freq[A[i]] += 1
        left_count[i] = prefix_freq[A[i]]

    # Counting suffix frequencies (for frequency(j, N, A[j]))
    for i in range(N - 1, -1, -1):
        suffix_freq[A[i]] += 1
        right_count[i] = suffix_freq[A[i]]

    count = 0
    right_counter = defaultdict(int)

    # We'll keep track of elements to the right of i for counting distinct elements
    distinct_right = 0

    for j in range(N - 1, -1, -1):
        if right_counter[A[j]] == 0:
            distinct_right += 1
        right_counter[A[j]] += 1
        right_count[j] = distinct_right

    pair_count = 0

    left_counter = defaultdict(int)
    distinct_left = 0

    for i in range(N):
        if left_counter[A[i]] == 0:
            distinct_left += 1
        left_counter[A[i]] += 1

        total_distinct = distinct_left + (right_count[i] - (1 if left_counter[A[i]] == 1 else 0))
        threshold = total_distinct // 2

        # Number of valid j for this i
        pair_count += max(0, (N - i - (threshold * 2)))
        pair_count %= MOD

    print(pair_count)

