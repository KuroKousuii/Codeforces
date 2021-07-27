s, v1, v2, t1, t2 = map(int, input().split())
res1, res2 = t1*2+s*v1, t2*2+s*v2
print("First" if res1 < res2 else "Second" if res2 < res1 else "Friendship")