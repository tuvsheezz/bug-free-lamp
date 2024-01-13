def euler_phi(n):
    phi = n
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            phi -= phi // p
            while n % p == 0:
                n //= p
    if n > 1:
        phi -= phi // n
    return phi


if __name__ == "__main__":
    n = int(input())
    print(euler_phi(n))
