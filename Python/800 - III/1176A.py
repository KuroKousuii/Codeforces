for _ in range(int(input())):
    x = int(input())
    cnt2, cnt3, cnt5 = 0, 0, 0
    while x % 2 == 0:
        cnt2 += 1
        x //= 2
    while x % 3 == 0:
        cnt3 += 1
        x //= 3
    while x % 5 == 0:
        cnt5 += 1
        x //= 5
    if x != 1:
        print(-1)
    else:
        print(3*cnt5+2*cnt3+cnt2)