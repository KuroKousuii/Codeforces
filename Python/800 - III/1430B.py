for _ in range(int(input())):
    n, k = map(int, input().split())
    total = 0
    arr = sorted([*map(int, input().split())], reverse=True)
    for i in range(0, k+1, 1):
        total += arr[i]
    print(total)