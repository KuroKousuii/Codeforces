*arr, d = map(int, input().split())
a, b, c = sorted(arr)
print(max(d-b+a, 0)+max(d-c+b, 0))
