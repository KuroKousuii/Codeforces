for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == c or b == d:
        print(abs(a-c)+abs(b-d))
    else:
        print(abs(a-c)+abs(b-d)+2)
