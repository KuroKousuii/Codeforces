n, k = map(int, input().split())
cnt = 0
while n <= k:
    n *= 3
    k *= 2
    cnt += 1
print(cnt)
