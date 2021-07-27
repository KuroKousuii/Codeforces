for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f'{-1} {-1}' if a*2 > b else f'{a} {a*2}')
