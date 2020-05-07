import numpy as np
from prettytable import PrettyTable
from _pydecimal import Decimal
from scipy.stats import f
from scipy.stats import t
from random import randrange
from math import sqrt
from math import fabs as fab


def a(first, second):
    need_a = 0
    for j in range(N):
        need_a += matrix_x[j][first - 1] * matrix_x[j][second - 1] / N
    return need_a


def find(number):
    a = 0
    for j in range(N):
        a += average_y[j] * matrix_x[j][number - 1] / 15
    return a


def check(b_lst, k):
    y_i = b_lst[0] + b_lst[1] * matrix[k][0] + b_lst[2] * matrix[k][1] + b_lst[3] * matrix[k][2] + \
          b_lst[4] * matrix[k][3] + b_lst[5] * matrix[k][4] + b_lst[6] * matrix[k][5] + b_lst[7] * matrix[k][6] + \
          b_lst[8] * matrix[k][7] + b_lst[9] * matrix[k][8] + b_lst[10] * matrix[k][9]
    return y_i


counter1 = 0
counter2 = 0

# Variant №208
for i in range(100):
    m, d = 3, 0
    p = 0.95
    N = 15

    x1_min, x1_max = -30, 0
    x2_min, x2_max = 10, 60
    x3_min, x3_max = 10, 35
    x01 = (x1_max + x1_min) / 2
    x02 = (x2_max + x2_min) / 2
    x03 = (x3_max + x3_min) / 2
    delta_x1 = x1_max - x01
    delta_x2 = x2_max - x02
    delta_x3 = x3_max - x03

    matrix_pfe = [
        [-1, -1, -1, +1, +1, +1, -1, +1, +1, +1],
        [-1, -1, +1, +1, -1, -1, +1, +1, +1, +1],
        [-1, +1, -1, -1, +1, -1, +1, +1, +1, +1],
        [-1, +1, +1, -1, -1, +1, -1, +1, +1, +1],
        [+1, -1, -1, -1, -1, +1, +1, +1, +1, +1],
        [+1, -1, +1, -1, +1, -1, -1, +1, +1, +1],
        [+1, +1, -1, +1, -1, -1, -1, +1, +1, +1],
        [+1, +1, +1, +1, +1, +1, +1, +1, +1, +1],
        [-1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0, 0],
        [+1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0, 0],
        [0, -1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0],
        [0, +1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0],
        [0, 0, -1.73, 0, 0, 0, 0, 0, 0, 2.9929],
        [0, 0, +1.73, 0, 0, 0, 0, 0, 0, 2.9929],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    matrix_x = [[] for x in range(N)]
    for i in range(len(matrix_x)):
        if i < 8:
            x_1 = x1_min if matrix_pfe[i][0] == -1 else x1_max
            x_2 = x2_min if matrix_pfe[i][1] == -1 else x2_max
            x_3 = x3_min if matrix_pfe[i][2] == -1 else x3_max

        else:
            x_lst = (
            matrix_pfe[i][0] * delta_x1 + x01, matrix_pfe[i][1] * delta_x2 + x02, matrix_pfe[i][2] * delta_x3 + x03)
            x_1, x_2, x_3 = x_lst
        matrix_x[i] = [x_1, x_2, x_3, x_1 * x_2, x_1 * x_3, x_2 * x_3, x_1 * x_2 * x_3, x_1 ** 2, x_2 ** 2, x_3 ** 2]

    adequacy, homogeneity = False, False
    while not adequacy:
        matrix_y = [[(8.0 + 5.3 * matrix_x[j][0] + 0.5 * matrix_x[j][1] + 5.6 * matrix_x[j][2] + 3.2 * matrix_x[j][0] *
                      matrix_x[j][0] + 0.7 * matrix_x[j][1] * matrix_x[j][1] + 4.1 * matrix_x[j][2] * matrix_x[j][2] + 8.9 *
                      matrix_x[j][0] * matrix_x[j][1] + 0.5 * matrix_x[j][0] * matrix_x[j][2] + 1.5 * matrix_x[j][1] *
                      matrix_x[j][2] + 1.2 * matrix_x[j][0] * matrix_x[j][1] * matrix_x[j][2] + randrange(0, 10) - 5) for i
                     in range(m)] for j in range(N)]
        average_x = []
        for column in range(len(matrix_x[0])):
            number_lst = []
            for rows in range(len(matrix_x)):
                number_lst.append(matrix_x[rows][column])
            average_x.append(sum(number_lst) / len(number_lst))

        average_y = []
        for rows in range(len(matrix_y)):
            average_y.append(sum(matrix_y[rows]) / len(matrix_y[rows]))

        matrix = [(matrix_x[i] + matrix_y[i]) for i in range(N)]
        mx_i = average_x
        my = sum(average_y) / 15

        unk = [
            [1, mx_i[0], mx_i[1], mx_i[2], mx_i[3], mx_i[4], mx_i[5], mx_i[6], mx_i[7], mx_i[8], mx_i[9]],
            [mx_i[0], a(1, 1), a(1, 2), a(1, 3), a(1, 4), a(1, 5), a(1, 6), a(1, 7), a(1, 8), a(1, 9), a(1, 10)],
            [mx_i[1], a(2, 1), a(2, 2), a(2, 3), a(2, 4), a(2, 5), a(2, 6), a(2, 7), a(2, 8), a(2, 9), a(2, 10)],
            [mx_i[2], a(3, 1), a(3, 2), a(3, 3), a(3, 4), a(3, 5), a(3, 6), a(3, 7), a(3, 8), a(3, 9), a(3, 10)],
            [mx_i[3], a(4, 1), a(4, 2), a(4, 3), a(4, 4), a(4, 5), a(4, 6), a(4, 7), a(4, 8), a(4, 9), a(4, 10)],
            [mx_i[4], a(5, 1), a(5, 2), a(5, 3), a(5, 4), a(5, 5), a(5, 6), a(5, 7), a(5, 8), a(5, 9), a(5, 10)],
            [mx_i[5], a(6, 1), a(6, 2), a(6, 3), a(6, 4), a(6, 5), a(6, 6), a(6, 7), a(6, 8), a(6, 9), a(6, 10)],
            [mx_i[6], a(7, 1), a(7, 2), a(7, 3), a(7, 4), a(7, 5), a(7, 6), a(7, 7), a(7, 8), a(7, 9), a(7, 10)],
            [mx_i[7], a(8, 1), a(8, 2), a(8, 3), a(8, 4), a(8, 5), a(8, 6), a(8, 7), a(8, 8), a(8, 9), a(8, 10)],
            [mx_i[8], a(9, 1), a(9, 2), a(9, 3), a(9, 4), a(9, 5), a(9, 6), a(9, 7), a(9, 8), a(9, 9), a(9, 10)],
            [mx_i[9], a(10, 1), a(10, 2), a(10, 3), a(10, 4), a(10, 5), a(10, 6), a(10, 7), a(10, 8), a(10, 9), a(10, 10)]]

        k = [my, find(1), find(2), find(3), find(4), find(5), find(6),
             find(7), find(8), find(9), find(10)]

        beta = np.linalg.solve(unk, k)
        print("Рівняння регресії")
        print("y = {:.3f} + {:.3f} * x1 + {:.3f} * x2 + {:.3f} * x3 + {:.3f} * x1x2 + {:.3f} * x1x3 + {:.3f} * x2x3"
              "+ {:.3f} * x1x2x3 + {:.3f} * x11^2 + {:.3f} * x22^2 + {:.3f} * x33^2 \n\nПеревірка"
              .format(beta[0], beta[1], beta[2], beta[3], beta[4], beta[5], beta[6], beta[7], beta[8], beta[9], beta[10]))
        for i in range(N):
            print("y{} = {:.3f} ≈ {:.3f}".format((i + 1), check(beta, i), average_y[i]))

        while not homogeneity:
            dispersion_y = [0.0 for x in range(N)]
            print("\n\n\n")
            for i in range(N):
                dispersion_i = 0
                for j in range(m):
                    dispersion_i += (matrix_y[i][j] - average_y[i]) ** 2
                dispersion_y.append(dispersion_i / (m - 1))
            f1 = m - 1
            f2 = N
            f3 = f1 * f2
            q = 1 - p
            Gp = max(dispersion_y) / sum(dispersion_y)

            print("Матриця планування:")

            x_norm = np.array(matrix_x)
            matrix_plan = np.array(matrix_y)
            my_table = np.hstack((x_norm, matrix_plan))
            table = PrettyTable()
            table.field_names = ["X1", "X2", "X3", "X1X2", "X1X3", "X2X3", "X1X2X3", "X1^2", "X2^2", "X3^2", "Y1", "Y2", "Y3"]
            for i in range(len(my_table)):
                table.add_row(my_table[i])

            print(table)

            print("Критерій Кохрена")

            f2 += 1
            partResult1 = q / (f2 - 1)
            params = [partResult1, f1, (f2 - 1 - 1) * f1]
            fisher = f.isf(*params)
            result = fisher / (fisher + (f2 - 1 - 1))
            Gt = Decimal(result).quantize(Decimal('.0001')).__float__()
            if Gt > Gp:
                print("Дисперсія однорідна при q = {:.2f}\n".format(q))
                homogeneity = True
            else:
                print("Дисперсія не однорідна при q = {:.2f}\n".format(q))
                m += 1

        dispersion_b2 = sum(dispersion_y) / (N * N * m)

        dispersion_b = sqrt(dispersion_b2)
        number_x = 10
        for column in range(number_x + 1):
            t_practice = 0
            t_theoretical = Decimal(abs(t.ppf(q / 2, f3))).quantize(Decimal('.0001')).__float__()
            for row in range(N):
                if column == 0:
                    t_practice += average_y[row] / N
                else:
                    t_practice += average_y[row] * matrix_pfe[row][column - 1]
            if fab(t_practice / dispersion_b) < t_theoretical:
                beta[column] = 0

        student_lst = list(beta)
        print("Отримане рівняння регресії з урахуванням критерія Стьюдента")
        print("y = {:.3f} + {:.3f} * x1 + {:.3f} * x2 + {:.3f} * 3 + {:.3f} * x1x2 + {:.3f} * x1x3 + {:.3f} * x2x3"
              "+ {:.3f} * x1x2x3 + {:.3f} * x11^2 + {:.3f} * x22^2 + {:.3f} * x33^2 \n\nПеревірка"
              .format(student_lst[0], student_lst[1], student_lst[2], student_lst[3], student_lst[4], student_lst[5],
                      student_lst[6], student_lst[7], student_lst[8], student_lst[9], student_lst[10]))
        for i in range(N):
            print("y{} = {:.3f} ≈ {:.3f}".format((i + 1), check(student_lst, i), average_y[i]))

        print("\nКритерій Фішера")
        d = 11 - student_lst.count(0)
        dispersion_ad = 0
        f4 = N - d
        for row in range(len(average_y)):
            dispersion_ad += (m * (average_y[row] - check(student_lst, row))) / (N - d)
        F_practice = dispersion_ad / dispersion_b2
        F_theoretical = Decimal(abs(f.isf(q, f4, f3))).quantize(Decimal('.0001')).__float__()
        if F_practice < F_theoretical:
            print("Рівняння регресії адекватне стосовно оригіналу")
            counter2 += 1
            adequacy = True
        else:
            counter1 += 1
            print("Рівняння регресії неадекватне стосовно оригіналу. Потрібно  провести експеремент повторно!")

print("З ефектом взаємодії {0}\nЗ квадратичними членами {1}".format(counter1, counter2))
