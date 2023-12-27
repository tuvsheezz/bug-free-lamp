def is_prime(x):
    if x == 2:
        return 1

    if x < 2 or x % 2 == 0:
        return 0

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return 0

    return 1


print(sum([is_prime(int(input())) for _ in range(int(input()))]))
