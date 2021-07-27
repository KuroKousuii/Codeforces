x = int(input())
arr = [*map(int, input().split())]
print(max(arr)-min(arr)+1-x)
