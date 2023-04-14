using CSharp.DoubleType;
using CSharp.IntegerType;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //For integers
            int[,] matrixA = { 
                {1,4}, 
                {2,3}, 
                {5,6} 
            };
            int[,] matrixB = { 
                {1,3,5}, 
                {2,4,6} 
            };

            int alpha = 2;
            int beta = 3;
            Benchmark<int, IntegerCalculation> calc = 
                new Benchmark<int, IntegerCalculation> (matrixA, matrixB, alpha, beta);
            int[,] resMatrix = calc.Dgemm();
            for (int i = 0; i < resMatrix.GetLength(0); i++)
            {
                for (int j = 0; j < resMatrix.GetLength(1); j++)
                {
                    Console.Write(resMatrix[i, j] + "\t");
                }
            }

            Console.WriteLine("\n");
            //For BigIntegers
            BigInteger[,] bigIntMatrixA = {
                {1,4},
                {2,3},
                {5,6}
            };
            BigInteger[,] bigIntMatrixB = {
                {1,3,5},
                {2,4,6}
            };
            BigInteger bigIntAlpha = 2;
            BigInteger bigIntBeta = 3;
            Benchmark<BigInteger, BigIntegerCalculation> calc2 = 
                new Benchmark<BigInteger, BigIntegerCalculation>(bigIntMatrixA, bigIntMatrixB, bigIntAlpha, bigIntBeta);
            BigInteger[,] resMatrix2 = calc2.Dgemm();
            for (int i = 0; i < resMatrix2.GetLength(0); i++)
            {
                for (int j = 0; j < resMatrix2.GetLength(1); j++)
                {
                    Console.Write(resMatrix2[i, j] + "\t");
                }
            }

            Console.WriteLine("\n");
            //For Doubles
            double[,] dMatrixA = {
                {1.0,4.0},
                {2.0,3.0},
                {5.0,6.0}
            };
            double[,] dMatrixB = {
                {1.0,3.0,5.0},
                {2.0,4.0,6.0}
            };
            double dAlpha = 2;
            double dBeta = 3;
            Benchmark<double, DoubleCalculation> calc3 =
                new Benchmark<double, DoubleCalculation>(dMatrixA, dMatrixB, dAlpha, dBeta);
            double[,] resMatrix3 = calc3.Dgemm();
            for (int i = 0; i < resMatrix3.GetLength(0); i++)
            {
                for (int j = 0; j < resMatrix3.GetLength(1); j++)
                {
                    Console.Write(resMatrix3[i, j] + "\t");
                }
            }
        }
    }
}
