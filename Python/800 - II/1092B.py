x = int(input())
check = 0
arr = sorted([*map(int, input().split())])
for i in range(1, x, 2):
    check += arr[i]-arr[i-1]
print(check)