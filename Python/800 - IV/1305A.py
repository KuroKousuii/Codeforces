for _ in range(int(input())):
    x = int(input())
    arr1 = sorted([*map(int, input().split())], reverse=True)
    arr2 = sorted([*map(int, input().split())], reverse=True)
    print(*arr1)
    print(*arr2)