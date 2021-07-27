for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]
    print("YES" if sum(arr) == k else "NO")