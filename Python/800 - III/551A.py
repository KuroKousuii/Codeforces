x = int(input())
ans = 1
arr = [*map(int, input().split())]
for i in range(x):
    start = 1
    for j in range(x):
        if arr[i] < arr[j]:
            start += 1
    print(start, end=" ")
print()