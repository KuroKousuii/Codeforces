for _ in range(int(input())):
    a, b, c = map(int, input().split())
    # print(f'{a*(c%2)} {(a-b)*(c//2)}')
    print((a-b)*(c//2)+a*(c%2))
