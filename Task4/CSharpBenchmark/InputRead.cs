using System;
using System.Collections.Generic;
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
            using (BinaryReader reader = new BinaryReader(File.Open("variable_data.bin", FileMode.Open)))
            {
                int rowMatrixA = Int32.Parse(reader.ReadString());
                int columnMatrixA = Int32.Parse(reader.ReadString());
                int rowMatrixB = 0;
                int columnMatrixB = 0;
                string empty;
                string[,] matrixA = new string[rowMatrixA, columnMatrixA];
                string[,] matrixB = new string[rowMatrixB, columnMatrixB];
                string alpha = null;
                string beta = null;
                while (reader.PeekChar() > -1)
                {
                    while (reader.ReadString() != null)
                    {
                        for (int row = 0; row < rowMatrixA; row++)
                        {
                            for (int column = 0; column < columnMatrixA; column++)
                            {
                                matrixA[row, column] = reader.ReadString();
                            }
                        }
                    }
                    empty = reader.ReadString();
                    rowMatrixB = Int32.Parse(reader.ReadString());
                    columnMatrixB = Int32.Parse(reader.ReadString());
                    matrixB = new string[rowMatrixB, columnMatrixB];
                    while (reader.ReadString() != null)
                    {
                        for (int row = 0; row < rowMatrixB; row++)
                        {
                            for (int column = 0; column < columnMatrixB; column++)
                            {
                                matrixB[row, column] = reader.ReadString();
                            }
                        }
                    }
                    empty = reader.ReadString();
                    alpha = reader.ReadString();
                    beta = reader.ReadString();
                }
                return new DataStruct { matrixA = matrixA, matrixB = matrixB, alpha = alpha, beta = beta, rowA = rowMatrixA, 
                    colA = columnMatrixA, rowB = rowMatrixB, colB = columnMatrixB};
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
                    matrixA[row, column] = Int32.Parse(data.matrixA[row, column]);
                }
            }
            for (int row = 0; row < data.rowB; row++)
            {
                for (int column = 0; column < data.colB; column++)
                {
                    matrixB[row, column] = Int32.Parse((data.matrixB[row, column]));
                }
            }
            alpha = Int32.Parse(data.alpha);
            beta = Int32.Parse(data.beta);  
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
