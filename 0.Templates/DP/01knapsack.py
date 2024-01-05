def knapsack(a, w):
    dp = [-1] * (w + 1)
    dp[0] = 0
    for x in a:
        for i in range(w, -1, -1):
            j = i - x[1]
            if j >= 0 and dp[j] != -1:
                dp[i] = max(dp[i], dp[j] + x[0])
    return max(dp)


if __name__ == "__main__":
    n, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(knapsack(a, w))
