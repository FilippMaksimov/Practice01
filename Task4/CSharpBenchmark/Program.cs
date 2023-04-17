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
            InputRead input = new InputRead();
            //For integers
            int[,] matrixA;
            int[,] matrixB;
            int alpha;
            int beta;
            input.getIntegerData(out matrixA, out matrixB, out alpha, out beta);
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
            BigInteger[,] bigIntMatrixA;
            BigInteger[,] bigIntMatrixB;
            BigInteger bigIntAlpha;
            BigInteger bigIntBeta;
            input.getBigIntegerData(out bigIntMatrixA, out bigIntMatrixB, out bigIntAlpha, out bigIntBeta);
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
            double[,] dMatrixA;
            double[,] dMatrixB;
            double dAlpha;
            double dBeta;
            input.getDoubleData(out dMatrixA, out dMatrixB, out dAlpha, out dBeta);
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
