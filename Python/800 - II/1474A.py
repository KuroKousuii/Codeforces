for _ in range(int(input())):
    x = int(input())
    s = input()
    prev = 0
    arr = []
    for i in range(x):
        if prev == 0:
            arr.append(1)
        elif prev == 1:
            if s[i] == '1':
                arr.append(1)
            else:
                arr.append(0)
        else:
            if s[i] == '1':
                arr.append(0)
            else:
                arr.append(1)
        prev = int(s[i])+arr[i]
    for i in arr:
        print(i, end="")
    print()
