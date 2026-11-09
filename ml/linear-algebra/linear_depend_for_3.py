import sys


def main():
    """
    Векторы линейно-независимые, если хотя бы один скалярный коэффициент не равен 0 и скалярное про-е равно 0 

    либо перебрать коэффициенты, либо просто систему решить

    Так как тут два вектора, то можно просто попробовать выразить один через другой

    можно тупо перебором в целом решить
    """
    matrix = []

    for i in range(3):
        line = list(map(int, input().split()))
        matrix.append(line)

    a1 = 0
    a2 = 0

    for i in range(-10, 12):
        a1 = i
        for j in range(-10, 12):
            a2 = j
            sum_x_y = list(((a1 * x) + (a2 * y)for x, y, z in zip(*matrix)))
            # print(f'sum_x_y {sum_x_y}')
            # print(f'res {matrix[2]}')
            
            if sum_x_y[0] == matrix[2][0] and sum_x_y[1] == matrix[2][1]:
                break

        if sum_x_y[0] == matrix[2][0] and sum_x_y[1] == matrix[2][1]:
            break

    if a1 == 11 and a2 == 11:
        print('NO_SOLUTION')
    else:
        print(a1, a2)

if __name__ == '__main__':
    main()
