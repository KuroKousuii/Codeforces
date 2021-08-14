for _ in range(int(input())):
    n, d = map(int, input().split())
    arr = [*map(int, input().split())]
    for i in range(1, n):
        while d - i >= 0 and arr[i] > 0:
            d -= i
            arr[i] -= 1
            arr[0] += 1
    print(arr[0])