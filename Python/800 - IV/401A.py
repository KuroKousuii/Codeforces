n, x = map(int, input().split())
arr = [*map(int, input().split())]
print((abs(sum(arr))+x-1)//x)