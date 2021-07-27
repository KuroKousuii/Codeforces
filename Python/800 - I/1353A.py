for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m*2 if n > 2 else m if n == 2 else 0)