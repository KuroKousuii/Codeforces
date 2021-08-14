n, k = map(int, input().split())
arr = [*map(str, input().split())]
ans = 0
for s in arr:
    ans += s.count('4') + s.count('7') <= k
print(ans)