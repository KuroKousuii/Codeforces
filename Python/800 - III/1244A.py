for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    need1, need2 = (a+c-1)//c, (b+d-1)//d
    if need1+need2 <= k:
        print(f'{need1} {need2}')
    else:
        print(-1)