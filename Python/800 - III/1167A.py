for _ in range(int(input())):
    x = int(input())
    s = input()
    ind = -1
    for i in range(x):
        if s[i] == '8':
            ind = i
            break
    print("YES" if ind != -1 and x-ind >= 11 else "NO")