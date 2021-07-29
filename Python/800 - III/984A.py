x = int(input())
arr = sorted([*map(int, input().split())])
print(arr[x//2-(x % 2 == 0)])
