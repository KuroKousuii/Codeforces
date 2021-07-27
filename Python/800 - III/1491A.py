import sys
n, q = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]
cnt1 = arr.count(1)
for i in range(q):
    tp, x = map(int, sys.stdin.readline().split())
    if tp == 1:
        cnt1 = cnt1+1 if not arr[x-1] else cnt1-1
        arr[x-1] = 1-arr[x-1]
    else:
        print(1 if cnt1 >= x else 0)