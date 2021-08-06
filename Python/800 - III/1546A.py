for _ in range(int(input())):
    x = int(input())
    up, down = [], []
    arr1 = [*map(int, input().split())]
    arr2 = [*map(int, input().split())]
    for i in range(x):
        if arr1[i] < arr2[i]:
            for j in range(arr2[i]-arr1[i]):
                up.append(i+1)
        elif arr1[i] > arr2[i]:
            for j in range(arr1[i]-arr2[i]):
                down.append(i+1)
    if len(up) != len(down):
        print(-1)
    else:
        print(len(up))
        for i in range(len(up)):
            print(f'{down[i]} {up[i]}')