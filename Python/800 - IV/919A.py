n, m = map(int, input().split())
ans = 1e9
for _ in range(n):
    a, b = map(int, input().split())
    ans = min(ans, m*a/b)
print(ans)