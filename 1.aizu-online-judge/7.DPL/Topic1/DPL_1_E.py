def edit_distance(s, t):
    n1 = len(s)
    n2 = len(t)
    dp = [[float("inf")] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        dp[i][0] = i

    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # change
            dp[i][j] = dp[i - 1][j - 1] + (s[i - 1] != t[j - 1])
            # delete S[i]
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            # delete T[j]
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    return dp[n1][n2]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
