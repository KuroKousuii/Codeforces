for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print(len([i for i in arr if i != min(arr)]))
