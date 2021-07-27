for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    cnt = 0
    for i in range(1, x):
        mx, mn = max(arr[i], arr[i-1]), min(arr[i], arr[i-1])
        check = mx/mn
        while check > 2:
            check /= 2
            cnt += 1
    print(cnt)