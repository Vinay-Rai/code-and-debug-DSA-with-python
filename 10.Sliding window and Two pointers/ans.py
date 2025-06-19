a = [1, 2, 3]
res = [[]]

for x in a:
    res += [s + [x] for s in res]

print(res)