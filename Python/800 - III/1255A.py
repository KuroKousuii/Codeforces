for _ in range(int(input())):
    x, y = map(int, input().split())
    check, mod = abs(x-y)//5, abs(x-y) % 5
    print(check+min((mod+1)//2, 1+(6-mod)//2))
