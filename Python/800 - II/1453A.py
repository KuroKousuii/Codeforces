for _ in range(int(input())):
    x, y = map(int, input().split())
    arr1 = {*map(int, input().split())}
    arr2 = [*map(int, input().split())]
    cnt = 0
    for i in arr2:
        if i in arr1:
            cnt += 1
    print(cnt)