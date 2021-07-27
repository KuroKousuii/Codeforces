for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    left, right = 0, x-1
    for i in range(x//2):
        print(arr[left], end=" ")
        print(arr[right], end=" ")
        left += 1
        right -= 1
    if left == right:
        print(arr[left])
    else:
        print()
