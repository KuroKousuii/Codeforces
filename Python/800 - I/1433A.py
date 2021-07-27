for _ in range(int(input())):
    x = int(input())
    print(10*(x % 10-1)+len(str(x))*(len(str(x))+1)//2)
