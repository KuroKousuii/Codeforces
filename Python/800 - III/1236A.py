for _ in range(int(input())):
    x, y, z = map(int, input().split())
    need1 = min(x, y//2)+min(y-min(x, y//2)*2, z//2)
    need2 = min(y, z//2)+min(x, (y-min(y, z//2))//2)
    print(max(need1, need2)*3)
    