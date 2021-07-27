import sys
x = int(sys.stdin.readline())
s = set(sys.stdin.readline().split()[1::]+sys.stdin.readline().split()[1::])
print("I become the guy." if len(s) == x else "Oh, my keyboard!")