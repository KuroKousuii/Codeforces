for _ in range(int(input())):
    s = input()
    arr = list(s)
    for i in range(len(s)):
        if i % 2 == 0:
            arr[i] = 'a' if arr[i] != 'a' else 'b'
        else:
            arr[i] = 'z' if arr[i] != 'z' else 'y'
    print("".join(arr))


