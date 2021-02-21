#테트로미노

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

def solve():    #모든 paper의 위치에서 테트로미노를 놓고 합산한 값을 찾음
    for i in range(n):
        for j in range(m):
            find(i,j)

def find(x,y):  #주어진 좌표 x, y에 대해 테트로미노 19가지 모양을 다 놓아보고 계산
    global result
    for i in range(19):
        sumNum=0
        for j in range(4):  #현재 x,y 좌표에 테트로미노를 놓음
            try:
                nx=x+tetromino[i][j][0] #x좌표
                ny=y+tetromino[i][j][1] #y좌표
                sumNum+=paper[nx][ny]
            except IndexError:  #테트로미노가 paper 밖으로 나가면 index에러 발생
                continue    #패스
        result=max(result,sumNum)

result=0
solve()
print(result)