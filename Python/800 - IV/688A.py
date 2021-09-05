n, d = map(int, input().split())
ans, cur = 0, 0
for i in range(d):
    s = input()
    if s != "1"*n:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 0
print(max(ans, cur))

