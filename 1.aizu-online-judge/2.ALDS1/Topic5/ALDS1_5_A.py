if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    dp = [False] * 2222
    dp[0] = True
    for aa in a:
        for i in range(2000, -1, -1):
            if i - aa >= 0 and dp[i - aa]:
                dp[i] = True
            elif i - aa < 0:
                break

    input()
    q = list(map(int, input().split()))
    for m in q:
        if dp[m]:
            print("yes")
        else:
            print("no")
