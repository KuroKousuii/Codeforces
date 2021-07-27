a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
x = int(input())
check = (a+b+c+4)//5+(d+e+f+9)//10
print("YES" if check <= x else "NO")