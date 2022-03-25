from typing import List
import heapq


class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self, k):
        root = None

        while k > 0:
            root = self.items[1]
            self.items[1] = self.items[-1]
            self.items.pop()
            self._percolate_down(1)
            k -= 1

        return root


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = BinaryMaxHeap()
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
