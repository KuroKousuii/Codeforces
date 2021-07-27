for _ in range(int(input())):
    x = int(input())
    arr = sorted([*map(int, input().split())])
    left, middle = 0, x
    for i in range(x):
        print(f'{arr[left]} {arr[middle]}', end=" ")
        left += 1
        middle += 1
    print()