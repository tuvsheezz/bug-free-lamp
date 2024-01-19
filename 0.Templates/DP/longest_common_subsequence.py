import sys

dp = [[0 for _ in range(1001)] for _ in range(1001)]
input = sys.stdin.readline


def LCS(s: str, t: str) -> int:
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            dp[i][j] = 0
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    return dp[len(s)][len(t)]


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input().strip()
        t = input().strip()
        print(LCS(s, t))
