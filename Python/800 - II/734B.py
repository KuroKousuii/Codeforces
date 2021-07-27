k2, k3, k5, k6 = map(int, input().split())
num256 = min(k2, k5, k6)
num32 = min(k3, k2-num256)
print(num32*32+num256*256)
