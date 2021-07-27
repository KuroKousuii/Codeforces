x = int(input())
arr = [*map(int, input().split())]
for i in range(x):
    arr[i] = arr[i]-1 if arr[i] % 2 == 0 else arr[i]
print(*arr)