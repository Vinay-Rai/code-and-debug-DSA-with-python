import sys
sys.setrecursionlimit(1 << 25)

MOD = 10**9 + 7

def solve_tree_beauty(n, A, B, parent, queries):
    from collections import defaultdict

    tree = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if parent[i] != 0:
            tree[parent[i]].append(i)

    in_time = [[0] * (n + 1) for _ in range(2)]
    out_time = [[0] * (n + 1) for _ in range(2)]
    time = [1, 1]

    def dfs(node, root_index, timer):
        in_time[root_index][node] = timer[0]
        timer[0] += 1
        for child in tree[node]:
            dfs(child, root_index, timer)
        out_time[root_index][node] = timer[0] - 1

    dfs(A, 0, [1])
    dfs(B, 1, [1])

    def is_ancestor(u, v, root_index):
        return in_time[root_index][u] <= in_time[root_index][v] <= out_time[root_index][u]

    answer_sum = 0
    k = 0
    for u, v in queries:
        u = (u + k) % n + 1
        v = (v + k) % n + 1
        if is_ancestor(u, v, 0) and is_ancestor(u, v, 1):
            beauty = 1
        else:
            beauty = 0
        k = beauty
        answer_sum = (answer_sum + beauty) % MOD

    return answer_sum


solve_tree_beauty(2,1,2,[0,1])
