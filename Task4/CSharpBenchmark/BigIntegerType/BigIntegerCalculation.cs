﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
using System.Threading;

namespace CSharp
{
    internal class BigIntegerCalculation : Calculations<BigInteger>
    {
        public override BigInteger[,] MatrixMultiplication(BigInteger[,] matrixA, BigInteger[,] matrixB)
        {
            int rowsA = matrixA.GetLength(0);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            BigInteger[,] res = new BigInteger[rowsA, columnsB];
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

        public override BigInteger[,] MatrixMultiplicationThreads(BigInteger[,] matrixA, BigInteger[,] matrixB, int threads)
        {
            int rowsA = matrixA.GetLength(0);
            int rowsB = matrixB.GetLength(0);
            int columnsB = matrixB.GetLength(1);
            BigInteger[,] res = new BigInteger[rowsA, columnsB];
            Parallel.For(0, rowsA - 1, new ParallelOptions { MaxDegreeOfParallelism = threads }, row =>
            {
                for (int column = 0; column < columnsB; column++)
                {
                    for (int i = 0; i < rowsB; i++)
                    {
                        res[row, column] += matrixA[row, i] * matrixB[i, column];
                    }
                }
            });
            return res;
        }

        public override BigInteger[,] MatrixSumm(BigInteger[,] matrixA, BigInteger[,] matrixB)
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

        public override BigInteger[,] MatrixTransposing(BigInteger[,] matrix)
        {
            int rowsMatrix = matrix.GetLength(0);
            int columnsMatrix = matrix.GetLength(1);
            BigInteger[,] transposedMatrix = new BigInteger[columnsMatrix, rowsMatrix];
            for (int row = 0; row < rowsMatrix; row++)
            {
                for (int column = 0; column < columnsMatrix; column++)
                {
                    transposedMatrix[column, row] = matrix[row, column];
                }
            }
            return transposedMatrix;
        }

        public override BigInteger[,] ScalarMultiplication(BigInteger[,] matrix, BigInteger scalar)
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
