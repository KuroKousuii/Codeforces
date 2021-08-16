s = input()
vad = "aeiou13579"
ans = 0
for c in s:
    ans += c in vad
print(ans)
