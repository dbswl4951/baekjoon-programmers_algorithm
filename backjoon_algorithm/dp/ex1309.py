#동물원
'''
사자를 배치할 수는 경우 3가지 존재
1. N번째 줄에 사자가 모두 없을 경우
2. N번째 줄에 왼쪽 칸에만 사자가 있는 경우
3. N번째 줄에 오른쪽 칸에만 사자가 있는 경우

1) 1번의 경우
현재 줄에 사자가 모두 없다면 윗줄에는 사자가 왼쪽 칸 배치 가능.
윗줄 오른쪽 칸 배치 가능.
윗줄 모두 미배치 가능.
2) 2번의 경우
현재 줄 왼쪽 칸에 사자가 있음으로 윗줄 오른쪽 칸에 사자 배치 가능.
윗줄 모두 미배치 가능.
3) 3번의 경우
현재 줄 오른쪽 칸에 사자가 있음으로 윗줄 왼쪽 칸에 사자 배치 가능.
윗줄 모두 미배치 가능.
'''
import sys

n=int(sys.stdin.readline().strip())
dp=[[0]*3 for _ in range(n+1)]
#dp[n][0]:n번째 줄에 사자가 모두 없을 경우, dp[n][1]:사자가 왼쪽에만 있을 경우, dp[n][2]:사자가 오른쪽에만 있을 경우
dp[1][0],dp[1][1],dp[1][2]=1,1,1
for i in range(2,n+1):
    dp[i][0]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901
    dp[i][1]=(dp[i-1][0]+dp[i-1][2])%9901
    dp[i][2]=(dp[i-1][0]+dp[i-1][1])%9901
print(sum(dp[n])%9901)