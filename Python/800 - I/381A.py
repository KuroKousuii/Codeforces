import collections
x = int(input())
dq = collections.deque([*map(int, input().split())])
counters = [0, 0]
check = 0
while len(dq) > 0:
    if dq[0] > dq[-1]:
        counters[check] += dq[0]
        dq.popleft()
    else:
        counters[check] += dq[-1]
        dq.pop()
    check = (check+1) % 2
for i in counters:
    print(i, end=" ")




