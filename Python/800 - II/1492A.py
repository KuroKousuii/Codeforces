for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    need = min((p+a-1)//a*a, (p+b-1)//b*b, (p+c-1)//c*c)
    print(need-p)
