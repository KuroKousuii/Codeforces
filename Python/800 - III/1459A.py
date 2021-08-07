for _ in range(int(input())):
    x = int(input())
    cnt1, cnt2 = 0, 0
    s1 = input()
    s2 = input()
    for i in range(x):
        cnt1 += s1[i] > s2[i]
        cnt2 += s1[i] < s2[i]
    print("RED" if cnt1>cnt2 else "BLUE" if cnt2>cnt1 else "EQUAL")
