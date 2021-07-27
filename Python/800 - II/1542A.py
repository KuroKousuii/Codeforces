for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    print("Yes" if len([i for i in arr if i%2]) == x else "No")