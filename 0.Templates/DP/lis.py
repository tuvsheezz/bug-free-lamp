import bisect


def lengthOfLIS(nums):
    dp = []
    for x in nums:
        if dp and dp[-1] >= x:
            ind = bisect.bisect_left(dp, x)
            dp[ind] = x
        else:
            dp.append(x)
    return len(dp)


if __name__ == "__main__":
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(lengthOfLIS(nums))
