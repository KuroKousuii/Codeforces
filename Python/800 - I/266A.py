x = int(input())
s = input()
sm = 0
for i in range(x):
    prev = s[i-1] if i > 0 else "-1"
    sm += s[i] == prev
    # print(s[i]+" "+prev)
print(sm)
