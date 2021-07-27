for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(0)
    elif x % 2:
        print(2 if x == 3 else 3)
    else:
        print(1 if x == 2 else 2)