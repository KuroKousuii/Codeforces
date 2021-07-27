for _ in range(int(input())):
    x = int(input())
    check = {*map(int, input().split())}
    print(x if len(check) == 1 else 1)
