import heapq

n = int(input())
heap = []
result = 0

for _ in range(n):
    a = int(input())
    heapq.heappush(heap, a)

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum = a + b
        result += sum
        heapq.heappush(heap, sum)

    print(result)
