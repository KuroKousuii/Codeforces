for _ in range(int(input())):
    x, ans = int(input()), 0
    arr = [*map(int, input().split())]
    for i in arr:
        ans += i
    print((ans-max(arr))/(x-1)+max(arr))
    