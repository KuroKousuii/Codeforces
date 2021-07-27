for _ in range(int(input())):
    x = int(input())
    arr = [i for i in range(1, x+1)]
    for i in range(0, x-x%2, 2):
        # print(f'{arr[i]} {arr[i+1]}')
        arr[i], arr[i+1] = arr[i+1], arr[i]
    if x%2:
        arr[x-1], arr[x-2] = arr[x-2], arr[x-1]
    print(*arr)