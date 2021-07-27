for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print(*[i for i in arr if i%2], end=" ")
    print(*[i for i in arr if i%2 == 0])