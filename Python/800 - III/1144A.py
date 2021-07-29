for _ in range(int(input())):
    s, check = "".join(sorted(input())), "abcdefghijklmnopqrstuvwxyz"
    print("Yes" if check.find(s) != -1 else "No")
