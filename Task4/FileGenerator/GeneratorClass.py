class WriteFile:
    @staticmethod
    def matrix_init():
        row_matrix = int(input("Ведите число строк в матрице =>"))
        column_matrix = int(input("Введите числок столбцов в матрице =>"))
        matrix = [["" for column in range(column_matrix)] for row in range(row_matrix)]
        for row in range(row_matrix):
            for column in range(column_matrix):
                matrix[row][column] = input(f"Введите элемент строки {row} столбца {column} =>")
        return matrix

    @staticmethod
    def scalar_input():
        alpha = input("Введите значение alpha =>")
        beta = input("Введите значение beta =>")
        return alpha, beta

    @staticmethod
    def file_write(matrix1, matrix2, alpha, beta):
        file_name = "../PythonBenchmark/variable_data.bin"
        with open(file_name, "wb") as f:
            matrix1_row = len(matrix1)
            matrix1_column = len(matrix1[0])

            matrix2_row = len(matrix2)
            matrix2_column = len(matrix2[0])

            matrix1_size_row = str(matrix1_row) + '\n'
            matrix1_size_column = str(matrix1_column) + '\n'
            bin_size_row1 = matrix1_size_row.encode()
            bin_size_column1 = matrix1_size_column.encode()

            matrix2_size_row = '\n' + str(matrix2_row) + '\n'
            matrix2_size_column = str(matrix2_column) + '\n'
            bin_size_row2 = matrix2_size_row.encode()
            bin_size_column2 = matrix2_size_column.encode()

            f.write(bin_size_row1)
            f.write(bin_size_column1)
            for row in matrix1:
                for item in row:
                    item = item + '\n'
                    bt = item.encode()
                    f.write(bt)

            f.write(bin_size_row2)
            f.write(bin_size_column2)
            for row in matrix2:
                for item in row:
                    item = item + '\n'
                    bt = item.encode()
                    f.write(bt)

            alpha_format = '\n' + alpha + '\n'
            beta_format = beta + '\n'
            bin_alpha = alpha_format.encode()
            bin_beta = beta_format.encode()
            f.write(bin_alpha)
            f.write(bin_beta)
