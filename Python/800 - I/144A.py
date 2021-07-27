import sys
x = int(sys.stdin.readline())
lst = [*map(int, sys.stdin.readline().split())]
total = lst.index(max(lst))+lst[::-1].index(min(lst))
print(total-(total >= x))
