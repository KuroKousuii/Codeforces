import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
print("HARD" if 1 in lst else "EASY")
