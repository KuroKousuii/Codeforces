x, arr = int(input()), []
need = 0
for i in range(x):
    a, b, c, d = map(int, input().split())
    if i == 0:
        need = a+b+c+d
    arr.append(a+b+c+d)
arr = sorted(arr, reverse=True)
for i in range(x):
    if arr[i] == need:
        print(i+1)
        break
