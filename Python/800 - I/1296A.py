for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    odd = [num for num in arr if num % 2 == 1]
    if len(odd) % 2 == 1:
        print("YES")
    else:
        if len(odd) == 0:
            print("NO")
        else:
            print("NO" if len(odd) == len(arr) else "YES")
