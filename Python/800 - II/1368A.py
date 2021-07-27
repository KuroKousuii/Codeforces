for _ in range(int(input())):
    a, b, c = map(int, input().split())
    cnt = 0
    while a <= c and b <= c:
        if a < b:
            a += b
        else:
            b += a
        a, b = b, a
        cnt += 1
    print(cnt)