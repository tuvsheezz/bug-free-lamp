if __name__ == "__main__":
    n = int(input())
    adj = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        u, k, *v = map(int, input().split())
        for x in v:
            adj[u - 1][x - 1] = 1

    for i in range(n):
        print(" ".join(map(str, adj[i])))
