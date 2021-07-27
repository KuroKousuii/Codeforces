def check(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total % 4 == 0


num = int(input())
while not check(num):
    num += 1
print(num)
