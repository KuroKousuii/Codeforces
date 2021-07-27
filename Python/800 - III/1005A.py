x = int(input())
arr, seq = [*map(int, input().split())], []
for i in range(x):
    prev = 0 if i == 0 else arr[i-1]
    if arr[i] <= prev:
        seq.append(prev)
seq.append(arr[x-1])
print(len(seq))
print(*seq)
