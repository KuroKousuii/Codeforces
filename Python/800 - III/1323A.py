for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    odd = [i+1 for i in range(len(arr)) if arr[i] % 2]
    even = [i+1 for i in range(len(arr)) if arr[i] % 2 == 0]
    if len(odd) >= 2:
        print(2)
        print(f'{odd[0]} {odd[1]}')
    elif len(even) >= 1:
        print(1)
        print(f'{even[0]}')
    else:
        print(-1)