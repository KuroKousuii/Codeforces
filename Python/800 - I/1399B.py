for _ in range(int(input())):
    x = int(input())
    total = 0
    arr1 = [*map(int, input().split())]
    arr2 = [*map(int, input().split())]
    for i in range(x):
        total += max(arr1[i]-min(arr1), arr2[i]-min(arr2))
    print(total)