import time
import os

from numpy.compat import long

import Benchmark as bench


def file_read():
    with open(os.path.abspath('../Data/variable_data.bin'), "rb") as f:
        s = f.readline()
        row_a = int(s)
        s = f.readline()
        column_a = int(s)
        matrix_a_float = [[0.00 for column in range(column_a)] for row in range(row_a)]
        matrix_a_int = [[0 for column in range(column_a)] for row in range(row_a)]
        matrix_a_long = [[long(0) for column in range(column_a)] for row in range(row_a)]
        for row in range(row_a):
            for column in range(column_a):
                bs = f.readline()
                s = bs.decode()
                s = s[:-1]
                matrix_a_float[row][column] = float(s)
                matrix_a_int[row][column] = int(s)
                matrix_a_long[row][column] = long(s)

        empty_line = f.readline()
        s = f.readline()
        row_b = int(s)
        s = f.readline()
        column_b = int(s)
        matrix_b_float = [[0.00 for column in range(column_b)] for row in range(row_b)]
        matrix_b_int = [[0 for column in range(column_b)] for row in range(row_b)]
        matrix_b_long = [[long(0) for column in range(column_b)] for row in range(row_b)]
        for row in range(row_b):
            for column in range(column_b):
                bs = f.readline()
                s = bs.decode()
                s = s[:-1]
                matrix_b_float[row][column] = float(s)
                matrix_b_int[row][column] = int(s)
                matrix_b_long[row][column] = long(s)

        empty_line_2 = f.readline()
        alpha_bs = f.readline()
        alpha_s = alpha_bs.decode()
        alpha_float = float(alpha_s)
        alpha_int = int(alpha_s)
        alpha_long = long(alpha_s)

        beta_bs = f.readline()
        beta_s = beta_bs.decode()
        beta_float = float(beta_s)
        beta_int = int(beta_s)
        beta_long = long(beta_s)
        return matrix_a_int, matrix_b_int, alpha_int, beta_int, matrix_a_float, \
            matrix_b_float, alpha_float, beta_float, matrix_a_long, matrix_b_long, alpha_long, beta_long


def launch_bench(thread):
    # For Integers
    matrix_a_int = file_read()[0]
    matrix_b_int = file_read()[1]
    alpha_int = file_read()[2]
    beta_int = file_read()[3]
    data_list_int = []
    operation_time = 0
    n = 0
    while n != 10:
        time_start_int = time.time()
        python_res_int = bench.dgemm_operation(matrix_a_int, matrix_b_int, alpha_int, beta_int, thread)
        operation_time += int((time.time() - time_start_int) * 10 ** 3)
        n = n + 1
    operation_time = int(operation_time / 10)
    items_a = len(matrix_a_int) * len(matrix_a_int[0])
    items_b = len(matrix_b_int) * len(matrix_b_int[0])
    total_sum = items_a + items_b
    data_list_int.append(operation_time)
    data_list_int.append(total_sum)

    # For floats(doubles)
    matrix_a_float = file_read()[4]
    matrix_b_float = file_read()[5]
    alpha_float = file_read()[6]
    beta_float = file_read()[7]
    data_list_float = []
    operation_time = 0
    n = 0
    while n != 10:
        time_start_float = time.time()
        python_res_float = bench.dgemm_operation(matrix_a_float, matrix_b_float, alpha_float, beta_float, thread)
        operation_time += int((time.time() - time_start_float) * 10 ** 6)
        n = n + 1
    operation_time = int(operation_time / 10)
    data_list_float.append(operation_time)
    data_list_float.append(total_sum)

    # For BigIntegers(long in Python)
    matrix_a_long = file_read()[8]
    matrix_b_long = file_read()[9]
    alpha_long = file_read()[10]
    beta_long = file_read()[11]
    data_list_long = []
    operation_time = 0
    n = 0
    while n != 10:
        time_start_long = time.time()
        python_res_long = bench.dgemm_operation(matrix_a_long, matrix_b_long, alpha_long, beta_long, thread)
        operation_time += int((time.time() - time_start_long) * 10 ** 6)
        n = n + 1
    operation_time = int(operation_time / 10)
    data_list_long.append(operation_time)
    data_list_long.append(total_sum)

    return data_list_int, data_list_float, data_list_long


def write_data(threads, data_int, data_long, data_float):
    try:
        with open(f"python{data_int[1]}_threads{threads}.bin", "wb") as f:
            title_int = "Python integer Data" + '\n'
            bt = title_int.encode()
            f.write(bt)
            for item in data_int:
                s = str(item) + '\n'
                bs = s.encode()
                f.write(bs)
            title_long = "Python long Data" + '\n'
            bt = title_long.encode()
            f.write(bt)
            for item in data_long:
                s = str(item) + '\n'
                bs = s.encode()
                f.write(bs)
            title_float = "Python float(double) Data" + '\n'
            bt = title_float.encode()
            f.write(bt)
            for item in data_float:
                s = str(item) + '\n'
                bs = s.encode()
                f.write(bs)
        print("Файл успешно записан")
    except IOError:
        print("Возникла ошибка. Файлы не удалось записать")


# Python Benchmark Launch
if __name__ == '__main__':
    write_data(0, launch_bench(thread=0)[0], launch_bench(thread=0)[2], launch_bench(thread=0)[1])
    write_data(2, launch_bench(thread=2)[0], launch_bench(thread=2)[2], launch_bench(thread=2)[1])
    write_data(4, launch_bench(thread=4)[0], launch_bench(thread=4)[2], launch_bench(thread=4)[1])
    write_data(8, launch_bench(thread=8)[0], launch_bench(thread=8)[2], launch_bench(thread=8)[1])


# C Sharp Benchmark Launch
# Note: in order to launch Java and C sharp exe files, there is needed to uncomment the below code:
'''
os.system(os.path.abspath('../CSharpBenchmark/bin/x64/Debug/CSharpBenchmark.exe'))
# Java Benchmark Launch
os.system(os.path.abspath('../JavaBenchmark/out/artifacts/Java_jar/Java.jar'))
'''