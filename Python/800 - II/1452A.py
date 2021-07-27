for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x*2 if x == y else max(x,y)*2-1)