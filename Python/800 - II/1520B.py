for _ in range(int(input())):
    x = int(input())
    check = int(str(x)[0] * len(str(x)))
    up = int(str(x)[0])
    print(9*(len(str(x))-1)+up-(check > x))