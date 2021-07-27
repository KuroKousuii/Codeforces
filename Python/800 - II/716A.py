n, c = map(int, input().split())
cnt = 0
arr = [*map(int, input().split())]
for i in range(n):
    prev = 0 if i == 0 else arr[i-1]
    if arr[i]-prev <= c:
        cnt += 1
    else:
        cnt = 1
print(cnt)