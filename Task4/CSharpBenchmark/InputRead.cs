using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    public class InputRead
    {
        private struct DataStruct
        {
            public int rowA;
            public int colA;
            public int rowB;
            public int colB;
            public string[,] matrixA;
            public string[,] matrixB;
            public string alpha;
            public string beta;
        }
        private static DataStruct getStringData()
        {
            using(FileStream fs = new FileStream("C:\\Users\\filma\\OneDrive\\Desktop\\ITMO.PythonCourse\\Practice01\\Task4\\CSharpBenchmark\\bin\\x64\\Debug\\variable_data.bin", FileMode.Open))
            {
                using (StreamReader reader = new StreamReader(fs, Encoding.UTF8))
                {
                    int rowMatrixA = int.Parse(reader.ReadLine());
                    int columnMatrixA = int.Parse(reader.ReadLine());

                    int rowMatrixB = 0;
                    int columnMatrixB = 0;
                    string[,] matrixA = new string[rowMatrixA, columnMatrixA];
                    for (int row = 0; row < rowMatrixA; row++)
                    {
                        for (int column = 0; column < columnMatrixA; column++)
                        {
                            matrixA[row, column] = reader.ReadLine();
                        }
                    }
                    rowMatrixB = int.Parse(reader.ReadLine());
                    columnMatrixB = int.Parse(reader.ReadLine());
                    string[,] matrixB = new string[rowMatrixB, columnMatrixB];
                    for (int row = 0; row < rowMatrixB; row++)
                    {
                        for (int column = 0; column < columnMatrixB; column++)
                        {
                            matrixB[row, column] = reader.ReadLine();
                        }
                    }
                    string alpha = reader.ReadLine();
                    string beta = reader.ReadLine();
                    return new DataStruct
                    {
                        matrixA = matrixA,
                        matrixB = matrixB,
                        alpha = alpha,
                        beta = beta,
                        rowA = rowMatrixA,
                        colA = columnMatrixA,
                        rowB = rowMatrixB,
                        colB = columnMatrixB
                    };
                }
            }
        }
        public void getIntegerData(out int[,] matrixA, out int[,] matrixB, out int alpha, out int beta)
        {
            DataStruct data = getStringData();
            matrixA = new int[data.rowA, data.colA];
            matrixB = new int[data.rowB, data.colB];
            for (int row = 0; row < data.rowA; row++)
            {
                for (int column = 0; column < data.colA; column++)
                {
                    matrixA[row, column] = int.Parse(data.matrixA[row, column]);
                }
            }
            for (int row = 0; row < data.rowB; row++)
            {
                for (int column = 0; column < data.colB; column++)
                {
                    matrixB[row, column] = int.Parse((data.matrixB[row, column]));
                }
            }
            alpha = int.Parse(data.alpha);
            beta = int.Parse(data.beta);  
        }
        public void getBigIntegerData(out BigInteger[,] matrixA, out BigInteger[,] matrixB, out BigInteger alpha, out BigInteger beta)
        {
            DataStruct data = getStringData();
            matrixA = new BigInteger[data.rowA, data.colA];
            matrixB = new BigInteger[data.rowB, data.colB];
            for (int row = 0; row < data.rowA; row++)
            {
                for (int column = 0; column < data.colA; column++)
                {
                    matrixA[row, column] = BigInteger.Parse(data.matrixA[row, column]);
                }
            }
            for (int row = 0; row < data.rowB; row++)
            {
                for (int column = 0; column < data.colB; column++)
                {
                    matrixB[row, column] = BigInteger.Parse((data.matrixB[row, column]));
                }
            }
            alpha = BigInteger.Parse(data.alpha);
            beta = BigInteger.Parse(data.beta);
        }
        public void getDoubleData(out double[,] matrixA, out double[,] matrixB, out double alpha, out double beta)
        {
            DataStruct data = getStringData();
            matrixA = new double[data.rowA, data.colA];
            matrixB = new double[data.rowB, data.colB];
            for (int row = 0; row < data.rowA; row++)
            {
                for (int column = 0; column < data.colA; column++)
                {
                    matrixA[row, column] = double.Parse(data.matrixA[row, column]);
                }
            }
            for (int row = 0; row < data.rowB; row++)
            {
                for (int column = 0; column < data.colB; column++)
                {
                    matrixB[row, column] = double.Parse(data.matrixB[row, column]);
                }
            }
            alpha = double.Parse(data.alpha);
            beta = double.Parse(data.beta);
        }
    }
}
