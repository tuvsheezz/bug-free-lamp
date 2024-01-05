if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(m):
            if i + a[j] <= n:
                dp[i + a[j]] = min(dp[i + a[j]], dp[i] + 1)
    print(dp[n])
