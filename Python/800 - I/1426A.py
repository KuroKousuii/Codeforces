for _ in range(int(input())):
    n, x = map(int, input().split())
    print(1 if n <= 2 else 1+(n+x-3)//x)
