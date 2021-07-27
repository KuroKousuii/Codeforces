for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    print("YES" if (a+b+c+n) % 3 == 0 and (a+b+c+n)//3 >= max(a, b, c) else "NO")
