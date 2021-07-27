for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]
    mx = max(arr)
    for i in range(n):
        arr[i] = mx-arr[i]
    if k % 2 == 0:
        mx = max(arr)
        for i in range(n):
            arr[i] = mx-arr[i]
    print(*arr)