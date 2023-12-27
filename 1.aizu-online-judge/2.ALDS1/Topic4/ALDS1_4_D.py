n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]


def n_loads(P):
    num = 0
    for _ in range(k):
        w_sum = 0
        while num < n and w_sum + w[num] <= P:
            w_sum += w[num]
            num += 1
    return num


P_lb, P_min = 0, max(w) * (n // k + 1)
while P_min - P_lb > 1:
    P_mid = (P_lb + P_min) // 2
    if n_loads(P_mid) < n:
        P_lb = P_mid
    else:
        P_min = P_mid

print(P_min)
