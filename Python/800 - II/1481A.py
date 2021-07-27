for _ in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    ok = True
    check = [s.count('R'), s.count('L'), s.count('U'), s.count('D')]
    check[0 if x > 0 else 1] -= abs(x)
    check[2 if y > 0 else 3] -= abs(y)
    for i in check:
        if i < 0:
            ok = False
    print("YES" if ok else "NO")