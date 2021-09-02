for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(1 - (x == 0))
    else:
        print(-1 if abs(x-y) % 2 else 2)