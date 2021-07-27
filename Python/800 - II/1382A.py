for _ in range(int(input())):
    x, y = map(int, input().split())
    arr1 = [*map(int, input().split())]
    arr2 = [*map(int, input().split())]
    ok = False
    for i in arr1:
        for j in arr2:
            if i == j and not ok:
                print("YES")
                print(f'1 {i}')
                ok = True
    if not ok:
        print("NO")
