using CSharp.DoubleType;
using CSharp.IntegerType;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
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
            DateTime timeStart1 = DateTime.Now; 
            int[,] resMatrix = calc.Dgemm();
            long operationTime = (long)(DateTime.Now.Subtract(timeStart1).TotalSeconds) * (10^6);

            Console.WriteLine("\n");
            //For BigIntegers
            BigInteger[,] bigIntMatrixA;
            BigInteger[,] bigIntMatrixB;
            BigInteger bigIntAlpha;
            BigInteger bigIntBeta;
            input.getBigIntegerData(out bigIntMatrixA, out bigIntMatrixB, out bigIntAlpha, out bigIntBeta);
            Benchmark<BigInteger, BigIntegerCalculation> calc2 = 
                new Benchmark<BigInteger, BigIntegerCalculation>(bigIntMatrixA, bigIntMatrixB, bigIntAlpha, bigIntBeta);
            DateTime timeStart2 = DateTime.Now;
            BigInteger[,] resMatrix2 = calc2.Dgemm();
            long operationTime2 = (long)(DateTime.Now.Subtract(timeStart2).TotalSeconds) * (10^6);


            Console.WriteLine("\n");
            //For Doubles
            double[,] dMatrixA;
            double[,] dMatrixB;
            double dAlpha;
            double dBeta;
            input.getDoubleData(out dMatrixA, out dMatrixB, out dAlpha, out dBeta);
            Benchmark<double, DoubleCalculation> calc3 =
                new Benchmark<double, DoubleCalculation>(dMatrixA, dMatrixB, dAlpha, dBeta);
            DateTime timeStart3 = DateTime.Now;
            double[,] resMatrix3 = calc3.Dgemm();
            long operationTime3 = (long)(DateTime.Now.Subtract(timeStart3).TotalSeconds) * (10^6);
        }
    }

}
