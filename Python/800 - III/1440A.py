for _ in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    s = input()
    print(s.count("1")*min(c1, c0+h)+s.count("0")*min(c0, c1+h))
