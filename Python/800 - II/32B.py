s = input()
ok = False
for i in range(len(s)):
    if ok:
        # print(f'Skip at {i}')
        ok = False
        continue
    if s[i] == '.':
        print(0, end="")
    else:
        if s[i:i+2] == "-.":
            print(1, end="")
        elif s[i:i+2] == "--":
            print(2, end="")
        ok = True