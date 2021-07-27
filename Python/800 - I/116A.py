t = int(input())
mx = -2e9
contain = 0
for i in range(t):
    x, y = map(int, input().split())
    contain += y-x
    mx = max(mx, contain)
print(mx)