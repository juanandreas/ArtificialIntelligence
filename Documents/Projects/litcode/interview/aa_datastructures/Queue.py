# import queue
# q = queue.Queue()

# q.put(1)
# x = q.get()
# print(x)

from collections import deque
q = deque()

q.append(1)
q.append(2)
q.append(3)

x = q.popleft()

print(list(q))
print(x)