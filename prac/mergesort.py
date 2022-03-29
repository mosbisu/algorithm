from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            if not arr1:
                return arr2
            if not arr2:
                return arr1

            result = []
            i = j = 0

            while i < len(arr1) or j < len(arr2):
                if i == len(arr1):
                    result.append(arr2[j])
                    j += 1
                    continue
                if j == len(arr2):
                    result.append(arr1[i])
                    i += 1
                    continue
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

            return result

        def mergesort(lst):
            if len(lst) == 1:
                return lst

            mid = len(lst) // 2
            L = mergesort(lst[:mid])
            R = mergesort(lst[mid:])

            return merge(L, R)

        return mergesort(nums)
