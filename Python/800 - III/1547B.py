for _ in range(int(input())):
    s = input()
    end = len(s)-1
    while len(s) > 0:
        if ord(s[0])-97 == end:
            s = s[1::]
        elif ord(s[-1])-97 == end:
            s = s[0:len(s)-1:]
        else:
            break
        end -= 1
    print("YES" if len(s) == 0 else "NO")