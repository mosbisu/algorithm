from collections import deque

N = int(input())
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(tree, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        for i in tree[node]:
            if not visited[i]:
                answer[i] = node
                q.append(i)
                visited[i] = True


bfs(tree, 1, visited)
for i in range(2, N+1):
    print(answer[i])

{
    0: [],
    1: [6, 4],
    2: [4],
    3: [6, 5],
    4: [1, 2, 7],
    5: [3],
    6: [1, 3],
    7: [4]
}
