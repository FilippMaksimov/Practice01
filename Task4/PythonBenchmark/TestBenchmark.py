from Task4.PythonBenchmark import Benchmark as test
import numpy as np

matrix_a = [[1, 4], [2, 3], [5, 6]]
matrix_b = [[1, 3, 5], [2, 4, 6]]
alpha = 2
beta = 3
matrix_res = test.dgemm_operation(matrix_a, matrix_b, alpha, beta)
print(matrix_res)

matrix_a = [[1.0, 4.0], [2.0, 3.0], [5.0, 6.0]]
matrix_b = [[1.0, 3.0, 5.0], [2.0, 4.0, 6.0]]
alpha = 2.0
beta = 3.0
matrix_res = test.dgemm_operation(matrix_a, matrix_b, alpha, beta)
print(matrix_res)

'''
barray = None
for row in range(len(matrix_a)):
    barray = bytearray(row)
filename = "TestFile.txt"
test_file = None
try:
    test_file = open(filename, "wb")
    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[0])):
            test_file.write(bytes(str(matrix_a[row][column]).encode("utf-8")))
    for row in range(len(matrix_b)):
        for column in range(len(matrix_b[0])):
            test_file.write(bytes(str(matrix_b[row][column]).encode("utf-8")))
    test_file.write(bytes(str(alpha).encode("utf-8")))
    test_file.write(bytes(str(beta).encode("utf-8")))
    test_file.write(barray)
finally:
    if test_file:
        test_file.close()

try:
    test_file = open(filename, "rb")
    first_item = test_file.read(2).decode("utf-8")
    second_item = test_file.read(10).decode("utf-8")
    print(test_file.readlines())
finally:
    if test_file:
        test_file.close()
'''

'''
file_name = "list.bin"
nparray = np.array([[1, 2], [1, 3], [1, 4]])
nparray.tofile(file_name)
'''

MATRIX = [['1.0', '4.0'], ['2.0', '3.0'], ['5.0', '6.0']]
MATRIX_SECOND = [['2.0', '3.0'], ['4.0', '5.0']]

with open("myFile.bin", "rb") as f:
    s = f.readline()
    row2 = int(s)
    s = f.readline()
    column2 = int(s)
    MATRIX2 = [[0.0 for column in range(column2)] for row in range(row2)]
    for row in range(row2):
        for column in range(column2):
            bs = f.readline()
            s = bs.decode()
            s = s[:-1]
            MATRIX2[row][column] = float(s)

    empty_line = f.readline()
    s = f.readline()
    row3 = int(s)
    s = f.readline()
    column3 = int(s)
    MATRIX3 = [[0.0 for column in range(column3)] for row in range(row3)]
    for row in range(row3):
        for column in range(column3):
            bs = f.readline()
            s = bs.decode()
            s = s[:-1]
            MATRIX3[row][column] = float(s)

print(MATRIX2)
print(MATRIX3)
