x = int(input())
s = input()
arr = [0]*10
for i in range(x):
    if s[i] == 'L':
        for j in range(0, 10, 1):
            if arr[j] == 0:
                arr[j] = 1
                break
    elif s[i] == 'R':
        for j in range(9, -1, -1):
            if arr[j] == 0:
                arr[j] = 1
                break
    else:
        arr[ord(s[i])-ord('0')] = 0
for i in arr:
    print(i, end="")
