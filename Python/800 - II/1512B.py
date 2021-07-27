for _ in range(int(input())):
    x = int(input())
    arr = []
    x1, y1, x2, y2 = -1, -1, -1, -1
    for i in range(x):
        s = list(input())
        arr.append(s)
    for i in range(x):
        for j in range(x):
            if arr[i][j] == '*':
                if x1 == -1:
                    x1 = i
                    y1 = j
                else:
                    x2 = i
                    y2 = j
    # print(f'{x1} {x2} {y1} {y2}')
    if x1 == x2:
        if x1-1 >= 0:
            arr[x1-1][y1], arr[x2-1][y2] = '*', '*'
        else:
            arr[x1+1][y1], arr[x2+1][y2] = '*', '*'
    elif y1 == y2:
        if y1-1 >= 0:
            arr[x1][y1-1], arr[x2][y2-1] = '*', '*'
        else:
            arr[x1][y1+1], arr[x2][y2+1] = '*', '*'
    else:
        arr[x1][y2], arr[x2][y1] = '*', '*'
    for s in arr:
        print("".join(s))