s1 = input()
s2 = input()
print(0 if s1.lower() == s2.lower() else 1 if s1.lower() > s2.lower() else -1)
