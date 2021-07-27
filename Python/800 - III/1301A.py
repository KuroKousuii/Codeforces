for _ in range(int(input())):
    s1 = input()
    s2 = input()
    s3 = input()
    ok = True
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] != s3[i] and s2[i] != s3[i]:
            ok = False
            break
        elif s1[i] == s2[i] and s1[i] != s3[i]:
            ok = False
            break
    print("YES" if ok else "NO")