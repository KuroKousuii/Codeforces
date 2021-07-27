import re
x, y = map(int, input().split())
s = input()
for i in range(y):
    s = re.sub("BG", "GB", s)
print(s)
