x = int(input())
arr = [*map(int, input().split())]
cnt, mx = 0, -1
for i in range(x):
    prev = 0 if i == 0 else arr[i-1]
    if arr[i] > prev:
        cnt += 1
    else:
        mx = max(cnt, mx)
        cnt = 1
print(max(cnt, mx))