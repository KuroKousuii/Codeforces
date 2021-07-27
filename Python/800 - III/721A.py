x = int(input())
cnt = 0
s, arr = input(), []
for c in s:
    if c == 'B':
        cnt += 1
    elif cnt:
        arr.append(cnt)
        cnt = 0
if cnt:
    arr.append(cnt)
print(len(arr))
print(*arr)