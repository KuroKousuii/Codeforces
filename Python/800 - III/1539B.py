n, q = map(int, input().split())
s = input()
arr, now = [], 0
for i in range(n):
    now += ord(s[i])-ord('a')+1
    arr.append(now)
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    left, right = 0 if l-1 < 0 else arr[l-1], arr[r]
    print(right-left)
