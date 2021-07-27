for _ in range(int(input())):
    x = int(input())
    arr = sorted([*map(int, input().split())])
    ok = False
    for i in range(x-1):
        ok |= arr[i+1]-arr[i] == 1
    print(1+ok)

