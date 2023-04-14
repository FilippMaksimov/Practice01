from Task4.Python import Benchmark as test

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
