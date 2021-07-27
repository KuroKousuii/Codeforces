for _ in range(int(input())):
    x = int(input())
    cnt = 0
    arr = [*map(int, input().split())]
    for i in arr:
        cnt = max(cnt, arr.count(i))
    print(cnt)
