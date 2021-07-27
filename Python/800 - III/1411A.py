for _ in range(int(input())):
    x = int(input())
    s = input()
    print("Yes" if len(s.rstrip(')')) < len(s)-len(s.rstrip(')')) else "No")