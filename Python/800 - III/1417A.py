for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    arr = sorted([*map(int, input().split())])
    for i in range(1, n, 1):
        cnt += (k-arr[i])//arr[0]
    print(cnt)