n, c = list(map(int, input().split()))
array = []
for _ in range(n):
    array.append(int(input()))
    array.sort()
start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start+end) // 2
    value = array[0]
    cnt = 1

    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
