a, b, c = map(int, input().split())
arr = [a+b+c, 2*(a+b), 2*(a+c), 2*(b+c)]
print(min(arr))