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

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, cur):
        smallest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


# 힙을 직접 구현해서 풀기
N = int(input())
result = []
heap = BinaryMinHeap()

for _ in range(N):
    x = int(input())

    if x == 0:                                 # 입력값이 0일 때
        if not heap:                           # 빈 배열이면 result에 0 추가
            result.append(0)
        else:                                  # 빈 배열이 아니면 result에 최솟값 추가
            result.append(heap.extract())
    else:
        heap.insert(x)                         # 0이 아니면 힙에 추가

for i in result:
    print(i)

# heapq를 이용한 풀이
N = int(input())
heap = []
result = []

for _ in range(N):
    x = int(input())

    if x == 0:                                 # 입력값이 0일 때
        if not heap:                           # 빈 배열이면 result에 0 추가
            result.append(0)
        else:                                  # 빈 배열이 아니면 result에 최솟값 추가
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)                # 0이 아니면 힙에 추가

for i in result:
    print(i)
