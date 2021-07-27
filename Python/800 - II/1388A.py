for _ in range(int(input())):
    x = int(input())
    if x <= 30:
        print("NO")
    else:
        print("YES")
        if x == 36 or x == 40 or x == 44:
            print(f'6 10 15 {x-31}')
        else:
            print(f'6 10 14 {x-30}')