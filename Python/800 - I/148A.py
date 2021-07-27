import sys
k = int(sys.stdin.readline())
l = int(sys.stdin.readline())
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
d = int(sys.stdin.readline())
cnt = 0
for i in range(1, d+1):
    cnt += i % k == 0 or i % l == 0 or i % m ==0 or i % n == 0
print(cnt)