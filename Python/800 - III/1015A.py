from collections import defaultdict
n, m = map(int, input().split())
mp = defaultdict(int)
for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r+1, 1):
        mp[j] += 1
print(m-len(mp))
for i in range(1, m+1, 1):
    if not mp[i]:
        print(i, end=" ")

