for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(a*a*4 if a*2 >= b else b*b)