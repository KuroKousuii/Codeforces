x = int(input())
s = input()
step = 1
cur = 0
while cur < x:
    print(s[cur], end="")
    cur += step
    step += 1
