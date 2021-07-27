for _ in range(int(input())):
    x = int(input())
    now = []
    start = 1
    while x:
        if x % 10:
            now.append(x % 10 * start)
        start *= 10
        x //= 10
    print(len(now))
    for i in now:
        print(i, end=" ")
    print()
