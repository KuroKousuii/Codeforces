for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = [*map(int, input().split())]
    if sum(arr) == x:
        print("NO")
    else:
        print("YES")
        check = 0
        for i in range(n):
            check += arr[i]
            if check == x:
                check -= arr[i]
                check += arr[i+1]
                arr[i], arr[i+1] = arr[i+1], arr[i]
            print(arr[i], end=" ")
        print()