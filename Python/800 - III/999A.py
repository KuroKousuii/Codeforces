from collections import deque
n, k = map(int, input().split())
deq = deque([*map(int, input().split())])
while len(deq) > 0:
    if deq[0] <= k:
        deq.popleft()
    elif deq[-1] <= k:
        deq.pop()
    else:
        break
print(n-len(deq))