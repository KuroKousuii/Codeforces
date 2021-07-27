for _ in range(int(input())):
    x = int(input())
    if x % 4 == 0:
        print("YES")
        for i in range(2, x + 1, 2):
            print(i, end=" ")
        for i in range(1, (x // 2 - 1) * 2, 2):
            print(i, end=" ")
        print(x//2*(x//2+1)-(x//2-1)*(x//2-1))
    else:
        print("NO")
