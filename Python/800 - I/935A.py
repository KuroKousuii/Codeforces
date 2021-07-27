check = 0
x = int(input())
for i in range(2, x+1):
    if x % i == 0:
        check += 1
print(check)
