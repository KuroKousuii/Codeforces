for _ in range(int(input())):
    n, x, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    mx, now = n-1, b-a
    print(min(mx, now+x))