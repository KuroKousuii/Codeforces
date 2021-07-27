for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    s = sum(arr)
    if s % x:
        print(-1)
    else:
        print(sum(v > s//x for v in arr))