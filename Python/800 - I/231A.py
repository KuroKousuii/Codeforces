k = int(input())
total = 0
for _ in range(k):
    a, b, c = map(int, input().split())
    total += 1 if a+b+c >= 2 else 0
print(total)
