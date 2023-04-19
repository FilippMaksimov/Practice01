using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    internal class Benchmark <M, N>
        where M: struct
        where N: Calculations<M>, new()
    {
        private M[,] matrixA;
        private M[,] matrixB;
        private M alpha;
        private M beta;

        public Benchmark(M[,] matrixA, M[,] matrixB, M alpha, M beta)
        {
            this.matrixA = matrixA;
            this.matrixB = matrixB;
            this.alpha = alpha;
            this.beta = beta;
        }
        public M[,] Dgemm(int threads)
        {
            lock (this)
            {
                Calculations<M> calc = new N();
                M[,] transA = calc.MatrixTransposing(matrixA);
                M[,] transB = calc.MatrixTransposing(matrixB);
                M[,] constRes = null;
                if (threads > 0)
                {
                    constRes = calc.ScalarMultiplication(calc.MatrixMultiplicationThreads(transA, transB, threads), alpha);
                }
                else if (threads == 0)
                {
                    constRes = calc.ScalarMultiplication(calc.MatrixMultiplication(transA, transB), alpha);
                }
                else
                {
                    throw new ArgumentException("Число потоков не может быть отрицательным!");
                }
                M[,] res = calc.MatrixSumm(constRes, calc.ScalarMultiplication(constRes, beta));
                return res;
            }
        }
    }
}
