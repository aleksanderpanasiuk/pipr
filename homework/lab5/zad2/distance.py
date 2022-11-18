def distance(n, A, B):
    if abs(A[0]) > n or abs(A[1]) > n or abs(B[0]) > n or abs(B[1]) > n:
        raise ValueError

    x_distance = flat_distance(A[0], B[0], n)
    y_distance = flat_distance(A[1], B[1], n)

    return x_distance + y_distance


def flat_distance(a, b, n):
    return min(abs(a - b), (2*n) - abs(a-b) + 1)
