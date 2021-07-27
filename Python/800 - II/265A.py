s = input()
t = input()
start = 0
for i in range(len(t)):
    if s[start] == t[i]:
        start += 1
print(start+1)