for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    if sum(arr) % 4 == 0:
        print("YES")
    elif sum(arr) % 2 == 0:
        print("NO" if arr.count(2) % 2 == 1 and arr.count(1) == 0 else "YES")
    else:
        print("NO")