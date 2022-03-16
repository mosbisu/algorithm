from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        lst = counts.most_common(k)

        return list(zip(*lst))[0]
