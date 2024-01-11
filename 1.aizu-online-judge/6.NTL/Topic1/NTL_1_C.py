import math

if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    ans = 1
    for i in a:
        ans = math.lcm(ans, i)
print(ans)
