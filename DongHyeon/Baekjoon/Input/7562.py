from collections import deque
n = int(input())

# 나이트가 이동할 수 있는 모든 지점
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

def bfs(x,y, x_e, y_e):
  q = deque()
  q.append([x,y])
  board[x][y] = 1
  while q:
    x, y = q.popleft()
    # 도착 지점에 도달하면 이때까지의 이동한 횟수를 출력 
    if x == x_e and y == y_e:
      return board[x][y] -1
    
    # 현재 위치에서 이동할 수 있는 모든 경우의 수
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      # 이동한 위치가 체스판 범위에서  벗어나지 않을 경우
      if 0 <= nx < l and 0 <= ny < l:

        # 만약 지금까지 나이트가 해당 지점을 방문하지 않았다면
        # 현재 위치를 큐에 저장
        # 이동 횟수 +1 
        if board[nx][ny] == 0:
          q.append([nx,ny])
          board[nx][ny] = board[x][y] + 1

for i in range(n):
    l = int(input())
    x, y = map(int,input().split())
    x_e, y_e = map(int,input().split())

    # 나이트가 해당 지점에 방문했는지 판단 
    # 방문 했다면 몇 회만에 방문했는지 저장
    board = [[0]*l for _ in range(l)]
    
    print(bfs(x,y,x_e,y_e))