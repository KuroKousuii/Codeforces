for _ in range(int(input())):
    x = int(input())
    ans, check = 0, 1
    arr = sorted([*map(int, input().split())], reverse=True)
    for i in range(x):
        check = check + 1 if arr[i] >= check else 1
        # print(f'Current check : {check}')
        ans = max(ans, check-1)
    print(max(check-1, ans))

