s = input()
total = 0
for i in range(len(s)):
    prev = 97 if i == 0 else ord(s[i-1])
    total += min(abs(ord(s[i])-prev), 26-abs(ord(s[i])-prev))
print(total)
