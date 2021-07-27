for _ in range(int(input())):
    n, k1, k2 = map(int,input().split())
    w, b = map(int, input().split())
    white, black = (k1+k2)//2, (2*n-k2-k1)//2
    print("YES" if white >= w and black >= b else "NO")