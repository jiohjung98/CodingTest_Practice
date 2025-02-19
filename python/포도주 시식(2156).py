n = int(input())
p = [0] * 10001
for i in range(1,n+1):
    p[i] = int(input())

dp = [0] * 10001
dp[1] = p[1]
dp[2] = p[1] + p[2]

for i in range(3, n+1):
    # 경우의 수 3가지
    # 1. 마지막 포도주 마시고 그 전 포도주 마셨을 때 - 현재 포도주로부터 -3 전까지 값 더하기
    # 2. 마지막 포도주 마시고 그 전 포도주 안마셨을 때 - 현재 포도주로부터 -2 전까지 값 더하기
    # 3. 마지막 포도주 안마셨을 때 - 현재 포도주로부터 -1 전까지 값 더하기
    dp[i] = max(p[i]+p[i-1]+dp[i-3], p[i]+dp[i-2], dp[i-1])

print(max(dp))
