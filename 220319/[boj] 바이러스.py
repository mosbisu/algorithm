from collections import deque

n = int(input())                      # 컴퓨터 수
m = int(input())                      # 연결된 컴퓨터 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):                    # 양방향 그래프
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []


def dfs(graph, node, visited):        # DFS 풀이
    visited.append(node)              # 현재 노드 방문처리
    for next in graph[node]:          # 현재 노드와 인접한 노드 확인
        if next not in visited:       # 방문 안한 노드면 재귀호출
            dfs(graph, next, visited)


dfs(graph, 1, visited)                # 1번 노드에 연결된 모든 값을 visited에 저장
print(len(visited) - 1)               # 1부터 시작이라서 -1


def bfs(start):                       # BFS 풀이
    visited = [start]                 # 첫 시작점
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:    # 방문한 적이 없으면
                q.append(adj)
                visited.append(adj)
    return visited


print(len(bfs(1)) - 1)                # 1부터 시작이라서 -1
