for _ in range(int(input())):
    x, y, k = map(int, input().split())
    print("YES" if (y-1)*x+x-1 == k else "NO")