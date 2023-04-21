from multiprocessing import Pool


def matrix_transposed(matrix):
    rows_matrix = len(matrix)
    columns_matrix = len(matrix[0])
    tran_matrix = [[0 for column in range(rows_matrix)] for row in range(columns_matrix)]
    for row in range(rows_matrix):
        for column in range(columns_matrix):
            tran_matrix[column][row] = matrix[row][column]
    return tran_matrix


def matrix_multiplication(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    rows_b = len(matrix_b)
    columns_b = len(matrix_b[0])
    res = [[0 for column in range(columns_b)] for row in range(rows_a)]
    for row in range(rows_a):
        for column in range(columns_b):
            for i in range(rows_b):
                res[row][column] += matrix_a[row][i] * matrix_b[i][column]
    return res


def scalar_multiplication(matrix, scalar):
    rows_matrix = len(matrix)
    columns_matrix = len(matrix[0])
    for row in range(rows_matrix):
        for column in range(columns_matrix):
            matrix[row][column] *= scalar
    return matrix


def matrix_sum(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    columns_b = len(matrix_b[0])
    if rows_a == rows_b and columns_a == columns_b:
        for row in range(rows_a):
            for column in range(columns_a):
                matrix_a[row][column] += matrix_b[row][column]
    return matrix_a


def separate_mult(data):
    row, matrix_a, matrix_b = data
    res = [0 for row in range(len(matrix_a))]
    for column in range(len(matrix_b[0])):
        for i in range(len(matrix_b)):
            res[column] += matrix_a[row][i] * matrix_b[i][column]
    return res


def matrix_multiplication_threads(matrix_a, matrix_b, threads):
    rows_a = len(matrix_a)
    with Pool(processes=threads) as pool:
        res = []
        data = [(row, matrix_a, matrix_b) for row in range(rows_a)]
        for row in pool.map(separate_mult, data):
            res.append(row)
        return res


def dgemm_operation(matrix_a, matrix_b, alpha, beta, thread):
    trans_a = matrix_transposed(matrix_a)
    trans_b = matrix_transposed(matrix_b)
    res_const = [[0 for column in range(len(trans_b[1]))] for row in range(len(trans_a))]
    if thread == 0:
        res_const = scalar_multiplication(matrix_multiplication(trans_a, trans_b), alpha)
    elif thread > 0:
        res_const = scalar_multiplication(matrix_multiplication_threads(trans_a, trans_b, thread), alpha)
    elif thread < 0:
        print("Количество потоков не может быть отрицательным")
    res = matrix_sum(res_const, scalar_multiplication(res_const, beta))
    return res
