for _ in range(int(input())):
    start = 1
    bound = int(input())
    while start*2 <= bound:
        start *= 2
    print(start-1)
