for _ in range(int(input())):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    dist = abs(yb-ya)+abs(xa-xb)
    if xa == xb == xf:
        if max(ya, yb) > yf > min(ya, yb):
            dist += 2
    elif ya == yb == yf:
        if max(xa, xb) > xf > min(xa, xb):
            dist += 2
    print(dist)
