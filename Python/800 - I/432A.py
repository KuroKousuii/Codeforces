n, k = map(int, input().split())
arr = [*map(int, input().split())]
cnt = 0
for i in arr:
    cnt += i+k <= 5
print(cnt//3)