sum = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    sum += b - a >= 2
print(sum)