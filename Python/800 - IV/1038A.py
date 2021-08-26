from collections import defaultdict
n, k = map(int, input().split())
s = input()
ans = 1e9
mp = defaultdict(int)
for i in s:
    mp[i] += 1
for i in range(ord('A'), ord('A')+k):
    ans = min(ans, mp[chr(i)])
print(ans*k)