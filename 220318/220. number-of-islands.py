from typing import List


class Solution:
    # stack
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                cnt += 1
                stack = [(row, col)]

                while stack:
                    x, y = stack.pop()
                    grid[x][y] = '0'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                            continue
                        stack.append((nx, ny))

        return cnt


class Solution2:
    # recursive(재귀)
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        def dfs_recursive(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return

            # 동서남북 방문처리
            grid[r][c] = '0'
            for i in range(4):
                dfs_recursive(r+dx[i], c+dy[i])
            return

        for r in range(m):
            for c in range(n):
                if grid[r][c] != '1':
                    continue

                cnt += 1
                dfs_recursive(r, c)

        return cnt
