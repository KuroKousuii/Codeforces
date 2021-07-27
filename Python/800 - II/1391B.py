for _ in range(int(input())):
    x, y = map(int, input().split())
    cnt = 0
    for i in range(x):
        s = input()
        if i == x-1:
            for j in range(y-1):
                cnt += s[j] == 'D'
        else:
            cnt += s[y-1] == 'R'
    print(cnt)