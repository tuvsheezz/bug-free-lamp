def big_pow(n, m, mod):
    if m == 0:
        return 1
    if m % 2 == 0:
        return big_pow(n * n % mod, m // 2, mod)
    else:
        return n * big_pow(n, m - 1, mod) % mod


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(big_pow(n, m, 1000000007))
