for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print(arr.count(1)+arr.count(3))
