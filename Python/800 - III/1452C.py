from collections import defaultdict
for _ in range(int(input())):
    s = input()
    sq, rd = 0, 0
    ans = 0
    for c in s:
        if c == '(':
            rd += 1
        elif c == '[':
            sq += 1
        elif c == ')' and rd > 0:
            ans += 1
            rd -= 1
        elif c == ']' and sq > 0:
            ans += 1
            sq -= 1
    print(ans)