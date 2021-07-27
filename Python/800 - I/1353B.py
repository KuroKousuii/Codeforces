for _ in range(int(input())):
    x, k = map(int, input().split())
    a = sorted([*map(int, input().split())])
    b = sorted([*map(int, input().split())], reverse=True)
    total = 0
    for i in range(x):
        if b[i] > a[i]:
            if k :
                a[i], b[i] = b[i], a[i]
                k -= 1
            else:
                break
    print(sum(a))
