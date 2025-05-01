from collections import deque

lst = deque([])

lst.append(100)
lst.append(100)
lst.append(300)
lst.appendleft(400)
print(lst)

lst.popleft()
print(lst)