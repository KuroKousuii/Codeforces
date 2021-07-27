for _ in range(int(input())):
    x = int(input())
    total = 0
    for i in range(1, x//2):
        total += 2**i
    for i in range(x//2, x):
        total -= 2**i
    print(total+2**x)

