for _ in range(int(input())):
    r, b, space = map(int, input().split())
    if r > b:
        r, b = b, r
    print("YES" if (space+1)*r >= b else "NO")