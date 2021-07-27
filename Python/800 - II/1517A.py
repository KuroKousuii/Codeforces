for _ in range(int(input())):
    x = int(input())
    if x % 2050:
        print(-1)
    else:
        check, need = x//2050, 0
        while check:
            need += check % 10
            check //= 10
        print(need)
