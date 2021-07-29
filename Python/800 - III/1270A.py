for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    arr1 = [*map(int, input().split())]
    arr2 = [*map(int, input().split())]
    print("YES" if max(arr1) > max(arr2) else "NO")