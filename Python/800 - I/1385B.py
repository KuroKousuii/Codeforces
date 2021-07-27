for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    new = []
    check = set()
    for i in arr:
        if i not in check:
            check.add(i)
            new.append(i)
    print(*new)
