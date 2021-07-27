for _ in range(int(input())):
    x = int(input())
    cntodd, cnteven = 0, 0
    arr = [*map(int, input().split())]
    for i, val in enumerate(arr):
        if val % 2 != i % 2:
            cntodd += val % 2
            cnteven += val % 2 == 0
    print(cntodd if cntodd == cnteven else -1)
