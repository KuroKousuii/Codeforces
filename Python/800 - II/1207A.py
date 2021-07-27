for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h < c:
        h, c = c, h
        p, f = f, p
    need1 = min(p, b//2)
    need2 = min((b-min(p, b//2)*2)//2, f)
    print(need1*h+need2*c)
