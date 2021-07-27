import sys
total = 0
x = int(sys.stdin.readline())
for i in map(int, sys.stdin.readline().split()):
    total += i/100
print(total / x * 100)