x = int(input())
arr = [*map(int, input().split())]
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    if a > 0:
        arr[a-1] += b-1
    if a < x-1:
        arr[a+1] += arr[a]-b
    arr[a] = 0
for line in arr:
    print(line)
