import sys

sys.setrecursionlimit(10**7)

pos = 0


def post_order(pre, in_, post, le, ri):
    global pos
    if le >= ri:
        return
    root = pre[pos]
    pos += 1

    ind = in_.index(root)

    post_order(pre, in_, post, le, ind)
    post_order(pre, in_, post, ind + 1, ri)

    post.append(root)


if __name__ == "__main__":
    n = int(input())
    pre = list(map(int, input().split()))
    in_ = list(map(int, input().split()))
    post = []
    post_order(pre, in_, post, 0, n)
    print(" ".join(map(str, post)))
