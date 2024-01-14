from math import gcd


def extended_euclid(a, b):
    """
    ax + by = gcd(a, b) => x, yを求める
    """
    _gcd = gcd(a, b)
    a = a // _gcd
    b = b // _gcd

    if b == 0:
        return [1, 0]
    else:
        xd, yd = extended_euclid(b, a % b)
        return (yd, xd - a // b * yd)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(*extended_euclid(a, b))
