for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    mn, mx = arr.index(min(arr)), arr.index(max(arr))
    if mn > mx:
        mn, mx = mx, mn
    # print(f'{mn} {mx}')
    print(min(mx+1, x-mn, mn+x-mx+1))
