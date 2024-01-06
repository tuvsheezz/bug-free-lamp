def coordinate_compression(a):
    s = sorted(list(set(a)))
    ranking = {x: i + 1 for i, x in enumerate(s)}
    return [ranking[x] for x in a]


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    print(*coordinate_compression(a))
