def knapsack(
    a: list[list[int]], w: int, by_weight: bool, is_zero_one: bool = True
) -> int:
    if by_weight:
        dp: list[int] = [-1] * (w + 1)
        dp[0] = 0
        for x in a:
            for i in range(w, -1, -1) if is_zero_one else range(w + 1):
                j = i - x[1]
                if j >= 0 and dp[j] != -1:
                    dp[i] = max(dp[i], dp[j] + x[0])
        return max(dp)
    else:
        sum_v = sum(x[0] for x in a)
        dp = [10**30] * (sum_v + 1)
        dp[0] = 0
        for x in a:
            for i in range(sum_v, -1, -1):
                j = i - x[0]
                if j >= 0 and dp[j] + x[1] <= w:
                    dp[i] = min(dp[i], dp[j] + x[1])
        return max(i for i in range(sum_v + 1) if dp[i] <= w)


if __name__ == "__main__":
    n, w = map(int, input().split())
    a: list[list[int]] = [list(map(int, input().split())) for _ in range(n)]
    print(knapsack(a, w, False, True))
