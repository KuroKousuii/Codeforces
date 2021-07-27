n, k = map(int, input().split())
sm = 0
lst = list(map(int, input().split()))
for i in lst:
    sm += 1 if i <= k else 2
print(sm)
