arr = sorted([*map(int, input().split())])
print(max(arr[2]+1-arr[0]-arr[1], 0))