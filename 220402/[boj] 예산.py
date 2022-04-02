n = int(input())
arr = list(map(int, input().split()))
m = int(input())
low = 0
high = max(arr)

while low <= high:
    mid = (low+high) // 2
    total = 0

    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)
