for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == l2 and r1 == r2:
        print(f'{l1} {r1}')
    elif l1 != l2 and r1 == r2:
        print(f'{l1} {l2}')
    elif l1 == l2 and r1 != r2:
        print(f'{r1} {r2}')
    else:
        print(f'{l1} {l2}')