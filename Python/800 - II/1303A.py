for _ in range(int(input())):
    s = input()
    total = 0
    arr = [i for i in range(len(s)) if s[i] == '1']
    for i in range(len(arr)-1):
        total += arr[i+1]-arr[i]-1
    print(total)