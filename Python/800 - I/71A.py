n = int(input())
for _ in range(n):
    s = input()
    print(s if len(s) < 11 else s[0]+str(len(s)-2)+s[-1])
