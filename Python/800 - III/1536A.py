for _ in range(int(input())):
    x = int(input())
    arr = [*map(int, input().split())]
    check = [i for i in arr if i < 0]
    if len(check) > 0:
        print("NO")
    else:
        print("YES")
        print("101")
        for i in range(1,101,1):
            print(i, end=" ")
        print(0)
