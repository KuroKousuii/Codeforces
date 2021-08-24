x = int(input())
print(x + 10-(x % 10) if x % 10 >= 5 else x - x % 10)