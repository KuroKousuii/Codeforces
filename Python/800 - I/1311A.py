for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        print(1 if (b-a) % 2 == 1 else 2)
    elif a > b:
        print(2 if (a-b) % 2 == 1 else 1)
    else:
        print(0)
