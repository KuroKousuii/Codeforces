for _ in range(int(input())):
    x, total = int(input()), 0
    arr = [*map(int, input().split())]
    pos = []
    for i in range(x):
        if arr[i] == 1:
            pos.append(i)
    for i in range(len(pos)-1):
        total += pos[i+1]-pos[i]-1
    print(total)
