n, m = map(int, input().split())
arr1 = [*map(int, input().split())]
arr2 = [*map(int, input().split())]
cnt1 = len([i for i in arr1 if i % 2 == 0])
cnt2 = len([i for i in arr2 if i % 2 == 0])
print(min(cnt1, m-cnt2)+min(n-cnt1, cnt2))
