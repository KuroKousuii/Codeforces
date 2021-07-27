for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print((sum(arr)+x-1)//x)