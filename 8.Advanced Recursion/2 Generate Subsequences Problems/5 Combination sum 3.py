#goood chatgpt solution


def combinationSum3(k, n):
    result = []

    def backtrack(start, path, total):
        # ✅ Base case: if we picked k numbers
        if len(path) == k:
            if total == n:
                result.append(path.copy())  # found valid combination
            return

        # 🚀 Explore numbers from 'start' to 9
        for i in range(start, 10):
            # Prune the branch if sum exceeds n
            if total + i > n:
                break  # no need to try further (since numbers are increasing)

            path.append(i)                  # choose
            backtrack(i + 1, path, total + i)  # explore
            path.pop()                      # un-choose (backtrack)

    backtrack(1, [], 0)
    return result