from typing import List
import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        result = set()
        nums2.sort()

        for n1 in nums1:
            idx = bisect.bisect_left(nums2, n1)

            if len(nums2) > idx and n1 == nums2[idx]:
                result.add(n1)

        return list(result)
