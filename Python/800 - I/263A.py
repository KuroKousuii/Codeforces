import sys
for i in range(5):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            print(abs(i-2)+abs(j-2))
            sys.exit(0)
