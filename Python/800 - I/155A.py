x = int(input())
cnt = 0
lst = [*map(int, input().split())]
mx, mn = lst[0], lst[0]
for i in range(1, x):
    if lst[i] > mx:
        cnt += 1
        mx = lst[i]
    elif lst[i] < mn:
        cnt +=1
        mn = lst[i]
print(cnt)
