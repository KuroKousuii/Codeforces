n, k = map(int, input().split())
cnt = 0
lst = list(map(int, input().split()))
# print(lst[k-1])
for i in range(len(lst)):
    # print(i)
    if lst[i] >= lst[k-1] and lst[i] > 0:
        cnt += 1
    else:
        break
print(cnt)
