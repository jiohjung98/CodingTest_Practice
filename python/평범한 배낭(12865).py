n, k = map(int, input().split())
bag = [(0,0)]
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w,v))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = bag[i]
    # j = 현재 수용 가능한 무게
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])
