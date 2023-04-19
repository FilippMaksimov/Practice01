using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    internal abstract class Calculations<M>
    {
        public abstract M[,] MatrixTransposing(M[,] matrix);
        public abstract M[,] MatrixMultiplication(M[,] matrixA, M[,] matrixB);
        public abstract M[,] ScalarMultiplication(M[,] matrix, M scalar);
        public abstract M[,] MatrixSumm(M[,] matrixA, M[,] matrixB);
        public abstract M[,] MatrixMultiplicationThreads(M[,] matrixA, M[,] matrixB, int threads);
    }
}
