import bisect


def lengthOfLIS(nums: list[int]) -> int:
    dp: list[int] = []
    for x in nums:
        if dp and dp[-1] >= x:
            ind = bisect.bisect_left(dp, x)
            dp[ind] = x
        else:
            dp.append(x)
    return len(dp)


if __name__ == "__main__":
    n = int(input())
    nums: list[int] = [int(input()) for _ in range(n)]
    print(lengthOfLIS(nums))
