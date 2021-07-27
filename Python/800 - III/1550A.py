for _ in range(int(input())):
    x = int(input())
    cnt = 0
    while cnt*cnt < x:
        cnt += 1
    print(cnt)