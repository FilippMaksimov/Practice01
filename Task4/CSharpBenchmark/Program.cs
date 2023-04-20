using CSharp.DoubleType;
using CSharp.IntegerType;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
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
            DataWrite(0);
            DataWrite(2);
            DataWrite(4);
            DataWrite(8);
        }
        static void DataWrite(int thread)
        {
            InputRead input = new InputRead();
            //For integers
            int[,] matrixA;
            int[,] matrixB;
            int alpha;
            int beta;
            input.getIntegerData(out matrixA, out matrixB, out alpha, out beta);
            Benchmark<int, IntegerCalculation> calc =
                new Benchmark<int, IntegerCalculation>(matrixA, matrixB, alpha, beta);
            DateTime timeStart1 = DateTime.Now;
            int[,] resMatrix = calc.Dgemm(thread);
            long operationTime1 = (long)(DateTime.Now.Subtract(timeStart1).TotalMilliseconds);

            long sum = matrixA.GetLength(0) * matrixA.GetLength(1) + matrixB.GetLength(0) * matrixB.GetLength(1);

            //For BigIntegers
            BigInteger[,] bigIntMatrixA;
            BigInteger[,] bigIntMatrixB;
            BigInteger bigIntAlpha;
            BigInteger bigIntBeta;
            input.getBigIntegerData(out bigIntMatrixA, out bigIntMatrixB, out bigIntAlpha, out bigIntBeta);
            Benchmark<BigInteger, BigIntegerCalculation> calc2 =
                new Benchmark<BigInteger, BigIntegerCalculation>(bigIntMatrixA, bigIntMatrixB, bigIntAlpha, bigIntBeta);
            DateTime timeStart2 = DateTime.Now;
            BigInteger[,] resMatrix2 = calc2.Dgemm(thread);
            long operationTime2 = (long)(DateTime.Now.Subtract(timeStart2).TotalMilliseconds);

            //For Doubles
            double[,] dMatrixA;
            double[,] dMatrixB;
            double dAlpha;
            double dBeta;
            input.getDoubleData(out dMatrixA, out dMatrixB, out dAlpha, out dBeta);
            Benchmark<double, DoubleCalculation> calc3 =
                new Benchmark<double, DoubleCalculation>(dMatrixA, dMatrixB, dAlpha, dBeta);
            DateTime timeStart3 = DateTime.Now;
            double[,] resMatrix3 = calc3.Dgemm(thread);
            long operationTime3 = (long)(DateTime.Now.Subtract(timeStart3).TotalMilliseconds);
            string path = "C:\\Users\\filma\\OneDrive\\Desktop\\ITMO.PythonCourse\\Practice01\\Task4\\CSharpBenchmark\\bin\\x64\\Debug\\csharp" + sum + "_thread" + thread.ToString() + ".bin";
            using (BinaryWriter writer = new BinaryWriter(File.Open(path, FileMode.OpenOrCreate)))
            {
                try
                {
                    writer.Write("CSharp Integer Data" + "\n");
                    writer.Write(operationTime1.ToString() + "\n");
                    writer.Write(sum.ToString() + "\n");
                    writer.Write("CSharp BigInteger Data" + "\n");
                    writer.Write(operationTime2.ToString() + "\n");
                    writer.Write(sum.ToString() + "\n");
                    writer.Write("CSharp Double Data" + "\n");
                    writer.Write(operationTime3.ToString() + "\n");
                    writer.Write(sum.ToString() + "\n");
                    Console.WriteLine("Файл записан успешно");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                }
            }
        }
    }

}
