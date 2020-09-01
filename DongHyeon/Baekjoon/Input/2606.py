from collections import deque
import sys
computer = int(sys.stdin.readline())
computer_edge = int(sys.stdin.readline())

# 그래프 생성 
graph = dict()
for i in range(computer_edge):
    a, b = map(int,sys.stdin.readline().split())
    if a in graph:
        graph[a].append(b)
    else: 
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

# BFS를 통해 1번 컴퓨터와 연결된 모든 노드 조사 
def bfs(graph, n):
    # 1번 컴퓨터와 연결되어 있다면 visited에 저장됨 
    visited = []
    q = deque()
    q.append(n)
    
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    # 자기 자신인 1번 컴퓨터를 뺀 나머지 컴퓨터 수
    return len(visited) - 1

print(bfs(graph, 1))