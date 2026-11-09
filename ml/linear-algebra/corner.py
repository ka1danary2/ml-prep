


import sys
import math


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())

    matrix = []

    for _ in range(2):
        matrix.append(list(map(int, input().split())))

    def l2_norma(w: list):
        accum = 0

        for el in w:
            accum += el ** 2

        return accum ** (1/2)

    v = l2_norma(matrix[0])
    u = l2_norma(matrix[1])

    a, b = matrix

    scalar = sum([x * y for x, y in zip(a, b)])

    cos_angle = scalar / (u * v)

    res2 = math.acos(cos_angle)

    print(int(math.degrees(res2)))


if __name__ == '__main__':
    main()
