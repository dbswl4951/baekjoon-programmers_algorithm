import sys
from collections import deque

_INF = float('inf')

def bellmanFord(N, dq, graph, visit, matrix, city):
    for i in range(N):
        for x in range(N):
            for v, w in graph[x]:
                if matrix[v] > matrix[x] + w - city[v]:
                    matrix[v] = matrix[x] + w - city[v]
                    if i == N-1:
                        visit[x] = True
                        dq.append(x)

def BFS(dq, graph, visit):
    while dq:
        x = dq.popleft()
        for v, w in graph[x]:
            if visit[v] == False:
                visit[v] = True
                dq.append(v)

def solution():
    N, S, E, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append((end, weight))

    city = list(map(int, sys.stdin.readline().split()))
    matrix = [_INF] * N
    visit = [False] * N
    matrix[S] = -city[S]

    dq = deque()
    bellmanFord(N, dq, graph, visit, matrix, city)
    BFS(dq, graph, visit)

    if visit[E] == True: print("Gee")
    elif matrix[E] == _INF: print('gg')
    else: print(-matrix[E])


solution()