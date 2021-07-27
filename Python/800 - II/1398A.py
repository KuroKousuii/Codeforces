for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print(f'{1} {2} {x}' if arr[0]+arr[1] <= arr[x-1] else -1)
    