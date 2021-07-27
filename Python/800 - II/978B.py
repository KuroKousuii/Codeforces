x = int(input())
s = input()
cnt = 0
for i in range(x-2):
    cnt += s[i] == 'x' and s[i+1] == 'x' and s[i+2] == 'x'
print(cnt)