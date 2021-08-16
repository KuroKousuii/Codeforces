n = int(input())
m = int(input())
it = 0
need = []
for i in range(n):
    sz = int(input())
    need.append(sz)
need = sorted(need, reverse=True)
while m > 0:
    m -= need[it]
    it += 1
print(it)