import sys
x, mn = int(input()), sys.maxsize
arr = [*map(int, input().split())]
id1, id2 = -1, -1
for i in range(0, x-1, 1):
    if mn > abs(arr[i+1]-arr[i]):
        id1 = i+1
        id2 = i+2
        mn = abs(arr[i+1]-arr[i])
print(f'{x} {1}' if mn > abs(arr[x-1]-arr[0]) else f'{id1} {id2}')