for _ in range(int(input())):
    x = int(input())
    ok = True
    lst = sorted([*map(int, input().split())])
    for i in range(1, x):
        if lst[i]-lst[i-1] > 1:
            ok = False
            break
    print("YES" if ok else "NO")

