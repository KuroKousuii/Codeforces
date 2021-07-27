for _ in range(int(input())):
    s = input()
    arr = []
    cnt = 0
    for i in s:
        if i == '1':
            cnt += 1
        else:
            if cnt != 0:
                arr.append(cnt)
            cnt = 0
    if cnt != 0:
        arr.append(cnt)
    print(sum(sorted(arr, reverse=True)[::2]))
