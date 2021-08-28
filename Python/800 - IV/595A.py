x, y = map(int, input().split())
cnt = 0
for i in range(x):
    arr = [*map(int, input().split())]
    for j in range(0, 2*y, 2):
        cnt += arr[j] == 1 or arr[j+1] == 1
print(cnt)