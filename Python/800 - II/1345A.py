for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if (a == 2 and b == 2) or (a == 1 or b == 1) else "NO")
    