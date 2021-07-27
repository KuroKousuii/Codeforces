s = input()
cnt = 0
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            if s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q':
                cnt += 1
print(cnt)
