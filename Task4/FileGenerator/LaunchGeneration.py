import GeneratorClass as file_class


wf = file_class.WriteFile()
matrix_a = wf.matrix_init()
matrix_b = wf.matrix_init()
alpha_beta = wf.scalar_input()
wf.file_write(matrix_a, matrix_b, alpha_beta[0], alpha_beta[1])
