for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print(x-arr.count(min(arr)))

