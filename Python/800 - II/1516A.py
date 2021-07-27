for _ in range(int(input())):
    x, k = map(int, input().split())
    arr = [*map(int, input().split())]
    for i in range(x):
        while arr[i] > 0 and k:
            arr[i] -= 1
            arr[x-1] += 1
            k -= 1
    print(*arr)