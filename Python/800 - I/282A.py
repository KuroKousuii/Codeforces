n = 0
k = int(input())
for _ in range(k):
    s = input()
    if s[-1]=='+' or s[0]=='+':
        n += 1
    else:
        n -= 1
print(n)