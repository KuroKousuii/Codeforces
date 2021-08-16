for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    for i in range(0, x, 2):
        print(f'{arr[i+1]*(-1)} {arr[i]}', end=" ")
    print()