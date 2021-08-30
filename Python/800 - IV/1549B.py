for _ in range(int(input())):
    n = int(input())
    a = ['X'] + list(input()) + ['X']
    m = 'X' + input() + 'X'
    ans = 0
    for i in range(1, n + 1):
        if m[i] == '1':
            if a[i] == '0':
                ans += 1
            elif a[i - 1] == '1':
                ans += 1
                a[i - 1] = '2'
            elif a[i + 1] == '1':
                ans += 1
                a[i + 1] = '2'
    print(ans)