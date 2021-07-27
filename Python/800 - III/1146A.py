s = input()
print(len(s) if s.count('a') > len(s)//2 else s.count('a')*2-1)
