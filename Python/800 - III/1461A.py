for _ in range(int(input())):
    x, k = map(int, input().split())
    ans = "abc"*((x+2)//3)
    print(ans[:x:])