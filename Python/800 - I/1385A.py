for _ in range(int(input())):
    arr = [*map(int, input().split())]
    if arr[0] == arr[1] and arr[0] == max(arr):
        print("YES")
        print(f'{arr[0]} {arr[2]} {arr[2]}')
    elif arr[1] == arr[2] and arr[1] == max(arr):
        print("YES")
        print(f'{arr[0]} {arr[0]} {arr[2]}')
    elif arr[0] == arr[2] and arr[0] == max(arr):
        print("YES")
        print(f'{arr[1]} {arr[0]} {arr[1]}')
    else:
        print("NO")