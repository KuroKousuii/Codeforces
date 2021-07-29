for _ in range(int(input())):
    x, cnt = int(input()), 0
    s = input()
    check = sorted(s)
    for i in range(x):
        cnt += check[i] != s[i]
    print(cnt)
