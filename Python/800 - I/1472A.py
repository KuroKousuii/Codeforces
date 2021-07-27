for _ in range(int(input())):
    a, b, c = map(int, input().split())
    start = 1
    while a % 2 == 0:
        a //= 2
        start *= 2
    while b % 2 == 0:
        b //= 2
        start *= 2
    print("YES" if start >= c else "NO")