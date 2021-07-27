for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    if sum(arr)<x:
        print(1)
    else:
        print(sum(arr)-x)