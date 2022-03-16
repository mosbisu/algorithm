from collections import defaultdict, Counter

# defaultdict를 이용한 비교 생략


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ht = defaultdict(int)
        count = 0

        for char in stones:
            ht[char] += 1

        for char in jewels:
            count += ht[char]

        return count

# Counter로 계산 생략


class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ht = Counter(stones)   # stones의 빈도 수 계산
        count = 0

        for char in jewels:    # 비교 없이 jewels의 빈도 수 합산
            count += ht[char]

        return count

# 파이썬다운 방식


class Solution3:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(char in jewels for char in stones)
