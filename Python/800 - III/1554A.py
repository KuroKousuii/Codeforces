for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    ans = arr[0]*arr[1]
    for i in range(1, x-1):
        ans = max(ans, arr[i]*arr[i+1])
    print(ans)