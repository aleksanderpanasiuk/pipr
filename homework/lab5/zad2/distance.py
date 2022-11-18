def distance(n, A, B):
    x_distance = flat_distance(A[0], B[0], n)
    y_distance = flat_distance(A[1], B[1], n)

    return x_distance + y_distance


def flat_distance(a, b, n):
    return min(abs(a - b), (2*n) - abs(a-b) + 1)
