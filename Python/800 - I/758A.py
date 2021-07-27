x = int(input())
arr = [*map(int, input().split())]
print(max(arr)*x-sum(arr))
