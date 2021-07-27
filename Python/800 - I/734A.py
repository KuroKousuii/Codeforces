x = int(input())
s = input()
print("Danik" if s.count('D') > s.count('A') else "Anton" if s.count('D') < s.count('A') else "Friendship")