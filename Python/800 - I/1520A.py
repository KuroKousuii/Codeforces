for _ in range(int(input())):
    x = int(input())
    s = input()+'0'
    store = []
    for i in range(x):
        if s[i] != s[i+1]:
            store.append(s[i])
    # for i in store:
    #     print(i, end=" ")
    print("NO" if len(set(store)) != len(store) else "YES")
