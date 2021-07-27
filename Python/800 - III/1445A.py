for line in range(int(input())):
    if line > 0:
        input()
    n, x = map(int, input().split())
    ok = True
    arr1 = sorted([*map(int, input().split())])
    arr2 = sorted([*map(int, input().split())], reverse=True)
    for i in range(n):
        if arr1[i]+arr2[i] > x:
            ok = False
            break
    print("Yes" if ok else "No")