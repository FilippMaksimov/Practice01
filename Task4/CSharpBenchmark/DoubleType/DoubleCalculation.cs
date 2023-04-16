using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp.DoubleType
{
    internal class DoubleCalculation: Calculations<double>
    {
        public DoubleCalculation() { }
        public override double[,] MatrixTransposing(double[,] matrix)
        {
            int rowsMatrix = matrix.GetLength(0);
            int columnsMatrix = matrix.GetLength(1);
            double[,] transposedMatrix = new double[columnsMatrix, rowsMatrix];
            for (int row = 0; row < rowsMatrix; row++)
            {
                for (int column = 0; column < columnsMatrix; column++)
                {
                    transposedMatrix[column, row] = matrix[row, column];
                }
            }
            return transposedMatrix;
        }

        public override double[,] MatrixMultiplication(double[,] matrixA, double[,] matrixB)
        {
            int rowsA = matrixA.GetLength(0);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            double[,] res = new double[rowsA, columnsB];
            for (int row = 0; row < rowsA; row++)
            {
                for (int column = 0; column < columnsB; column++)
                {
                    for (int i = 0; i < rowsB; i++)
                    {
                        res[row, column] += matrixA[row, i] * matrixB[i, column];
                    }
                }
            }
            return res;
        }

        public override double[,] ScalarMultiplication(double[,] matrix, double scalar)
        {
            int rowsMatrix = matrix.GetLength(0);
            int columnsMatrix = matrix.GetLength(1);
            for (int row = 0; row < rowsMatrix; row++)
            {
                for (int column = 0; column < columnsMatrix; column++)
                {
                    matrix[row, column] *= scalar;
                }
            }
            return matrix;
        }

        public override double[,] MatrixSumm(double[,] matrixA, double[,] matrixB)
        {
            int rowsA = matrixA.GetLength(0);
            int columnsA = matrixA.GetLength(1);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            if (rowsA == rowsB && columnsA == columnsB)
            {
                for (int row = 0; row < rowsA; row++)
                {
                    for (int column = 0; column < columnsA; column++)
                    {
                        matrixA[row, column] += matrixB[row, column];
                    }
                }
            }
            return matrixA;
        }
    }
}
