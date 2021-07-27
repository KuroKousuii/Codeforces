def check(ss):
    rev = ss[::-1]
    return rev == ss


for _ in range(int(input())):
    s = input()
    s1, s2 = "a"+s, s+"a"
    if not check(s1):
        print("YES")
        print(s1)
    elif not check(s2):
        print("YES")
        print(s2)
    else:
        print("NO")