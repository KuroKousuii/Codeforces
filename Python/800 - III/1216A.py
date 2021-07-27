x = int(input())
s = list(input())
cnt = 0
for i in range(0, x, 2):
    if s[i] == s[i+1]:
        cnt += 1
        if s[i] == 'a':
            s[i] = 'b'
        else:
            s[i] = 'a'
print(cnt)
print("".join(s))
