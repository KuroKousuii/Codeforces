for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    check = set()
    for i in arr:
        if i in check:
            i += 1
        check.add(i)
    print(len(check))