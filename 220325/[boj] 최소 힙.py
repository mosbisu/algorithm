import sys
import heapq
input = sys.stdin.readline


class BinaryMinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur, parent = parent, cur // 2

    def insert(self, val: int):
        self.items.append(val)
        self._percolate_up()

    def _percolate_down(self, cur):
        smallest, left, right = cur, cur*2, cur*2+1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def extract(self):
        if len(self) < 1:
            return 0

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


# 힙을 직접 구현해서 풀기
N = int(input())
arr = [int(input()) for _ in range(N)]
result = []
heap = BinaryMinHeap()

for x in arr:
    if x == 0:                             # 입력값이 0일 때
        if len(heap) == 0:                 # 빈 배열이면 0 추가
            result.append(0)
            continue
        else:                              # 빈 배열이 아니면 최솟값 추가
            result.append(heap.extract())
            continue

    heap.insert(x)

for i in result:
    print(i)

# heapq를 이용한 풀이
N = int(input())
X = []
result = []

for _ in range(N):
    x = int(input())

    if x == 0:                             # 입력값이 0일 때
        if len(X) == 0:                    # 빈 배열이면 0 추가
            result.append(0)
        else:                              # 빈 배열이 아니면 최솟값 추가
            result.append(heapq.heappop(X))
    else:
        heapq.heappush(X, x)

for i in result:
    print(i)
