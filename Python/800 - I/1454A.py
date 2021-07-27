for _ in range(int(input())):
    x = int(input())
    for i in range(x):
        print((i+x-1) % x + 1, end=" ")
    print()