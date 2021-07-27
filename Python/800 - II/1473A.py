for _ in range(int(input())):
    x, k = map(int, input().split())
    arr = sorted([*map(int, input().split())])
    print("YES" if arr[-1] <= k or arr[0]+arr[1] <= k else "NO")
    