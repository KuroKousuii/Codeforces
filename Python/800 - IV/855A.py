from collections import defaultdict
x = int(input())
mp = defaultdict(int)
for i in range(x):
    s = input()
    print("NO" if not mp[s] else "YES")
    mp[s] += 1