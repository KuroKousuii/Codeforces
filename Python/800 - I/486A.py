import sys
x = int(sys.stdin.readline())
print(x//2 if x % 2 == 0 else (-(x+1))//2)