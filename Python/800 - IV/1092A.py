for _ in range(int(input())):
    a, b = map(int, input().split())
    check = "abcdefghijklmnopqrstuvwxyz"
    print((check[:b:]*((a+b-1)//b))[:a:])