from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        leaves = []                   # 리프 노드를 추가할 빈 배열

        for a, b in edges:            # 양방향 그래프
            graph[a].append(b)
            graph[b].append(a)

        if n <= 1:                    # 루트 노드만 입력되면 [0] 반환
            return [0]

        for i in range(n):
            if len(graph[i]) == 1:    # 리프 노드일 경우 leaves에 추가
                leaves.append(i)

        while n > 2:                  # 루트 노드만 남을 때까지 반복 제거
            n -= len(leaves)          # 루트 노드가 2개일 수도 있으므로 2개까지 반복
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
