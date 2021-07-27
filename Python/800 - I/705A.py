import sys
x = int(sys.stdin.readline())
s = ""
for i in range(x):
    s += "I hate " if i % 2 == 0 else "I love "
    if i < x-1:
        s += "that "
s += "it"
print(s)