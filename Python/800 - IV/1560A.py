def check(n):
    if n % 10 == 3:
        return False
    cur = 0
    while n:
        cur += n % 10
        n //= 10
    return True if cur % 3 else False


for _ in range(int(input())):
    x = int(input())
    start = 1
    while True:
        if check(start):
            # print(f"Now : {start}")
            x -= 1
            if x == 0:
                break
        start += 1
    print(start)
