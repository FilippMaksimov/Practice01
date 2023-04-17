import time

from Task4.PythonBenchmark import Benchmark as bench


def file_read():
    with open("variable_data.bin", "rb") as f:
        s = f.readline()
        row_a = int(s)
        s = f.readline()
        column_a = int(s)
        matrix_a_float = [[0.00 for column in range(column_a)] for row in range(row_a)]
        matrix_a_int = [[0 for column in range(column_a)] for row in range(row_a)]
        for row in range(row_a):
            for column in range(column_a):
                bs = f.readline()
                s = bs.decode()
                s = s[:-1]
                matrix_a_float[row][column] = float(s)
                matrix_a_int[row][column] = int(s)

        empty_line = f.readline()
        s = f.readline()
        row_b = int(s)
        s = f.readline()
        column_b = int(s)
        matrix_b_float = [[0.00 for column in range(column_b)] for row in range(row_b)]
        matrix_b_int = [[0 for column in range(column_b)] for row in range(row_b)]
        for row in range(row_b):
            for column in range(column_b):
                bs = f.readline()
                s = bs.decode()
                s = s[:-1]
                matrix_b_float[row][column] = float(s)
                matrix_b_int[row][column] = int(s)

        empty_line_2 = f.readline()
        alpha_bs = f.readline()
        alpha_s = alpha_bs.decode()
        alpha_float = float(alpha_s)
        alpha_int = int(alpha_s)

        beta_bs = f.readline()
        beta_s = beta_bs.decode()
        beta_float = float(beta_s)
        beta_int = int(beta_s)
        return matrix_a_int, matrix_b_int, alpha_int, beta_int, matrix_a_float, matrix_b_float, alpha_float, beta_float


def launch_bench():
    matrix_a_int = file_read()[0]
    matrix_b_int = file_read()[1]
    alpha_int = file_read()[2]
    beta_int = file_read()[3]
    data_list_int = []
    time_start_int = time.time()
    python_res_int = bench.dgemm_operation(matrix_a_int, matrix_b_int, alpha_int, beta_int)
    time_end_int = time.time()

    matrix_a_float = file_read()[4]
    matrix_b_float = file_read()[5]
    alpha_float = file_read()[6]
    beta_float = file_read()[7]
    data_list_float = []
    time_start_int = time.time()
    python_res_float = bench.dgemm_operation(matrix_a_float, matrix_b_float, alpha_float, beta_float)
    time_end_float = time.time()
    return python_res_int, python_res_float


print(launch_bench().__getitem__(0))
print(launch_bench().__getitem__(1))
