using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CSharp.IntegerType
{
    internal class IntegerCalculation : Calculations<int>
    {
        public override int[,] MatrixMultiplication(int[,] matrixA, int[,] matrixB)
        {
            int rowsA = matrixA.GetLength(0);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            int[,] res = new int[rowsA, columnsB];
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

        public override int[,] MatrixMultiplicationThreads(int[,] matrixA, int[,] matrixB, int threads)
        {
            int rowsA = matrixA.GetLength(0);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            int[,] res = new int[rowsA, columnsB];
            List<Thread> threadsList = new List<Thread>();
            CountdownEvent countdown = new CountdownEvent(rowsA);
            for (int i = 0; i < threads; i++)
            {
                threadsList.Add(new Thread(() =>
                {
                    lock (res)
                    {
                        for (int row = 0; row < rowsA; row++)
                        {
                            for (int column = 0; column < columnsB; column++)
                            {
                                for (int j = 0; j < rowsB; j++)
                                {
                                    res[row, column] += matrixA[row, j] * matrixB[j, column];
                                }
                            }
                        }
                    }
                    countdown.Signal();
                }));
                threadsList[i].Start();
            }
            countdown.Wait();
            return res;
        }

        public override int[,] MatrixSumm(int[,] matrixA, int[,] matrixB)
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

        public override int[,] MatrixTransposing(int[,] matrix)
        {
            int rowsMatrix = matrix.GetLength(0);
            int columnsMatrix = matrix.GetLength(1);
            int[,] transposedMatrix = new int[columnsMatrix, rowsMatrix];
            for (int row = 0; row < rowsMatrix; row++)
            {
                for (int column = 0; column < columnsMatrix; column++)
                {
                    transposedMatrix[column, row] = matrix[row, column];
                }
            }
            return transposedMatrix;
        }

        public override int[,] ScalarMultiplication(int[,] matrix, int scalar)
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
    }
}
