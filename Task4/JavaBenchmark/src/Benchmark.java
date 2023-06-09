import BenchmarkCalculation.Calculations;
import BenchmarkCalculation.CalculationsFactory;

public class Benchmark<M> {
    private M[][] matrixA;
    private M[][] matrixB;
    private M alpha;
    private M beta;
    private Class<M> someClass;
    public Benchmark(Class<M> someClass, M[][] matrixA, M[][] matrixB, M alpha, M beta) {
        this.matrixA = matrixA;
        this.matrixB = matrixB;
        this.alpha = alpha;
        this.beta = beta;
        this.someClass = someClass;
    }
    //Внести изменения - реализовать ввод параметра для количества потоков
    public M[][] dgemm(int thread) throws Exception {
        synchronized (this) {
            Calculations<M> calc = new CalculationsFactory<M>(someClass).getSomeClass();
            M[][] transA = calc.matrixTransposing(matrixA);
            M[][] transB = calc.matrixTransposing(matrixB);
            M[][] constRes = null;
            if (thread > 0) {
                constRes = calc.scalarMultiplication(calc.matrixMultiplicationThreads(transA, transB, thread), alpha);
            }
            else if (thread == 0) {
                constRes = calc.scalarMultiplication(calc.matrixMultiplication(transA, transB), alpha);
            }
            else {
                throw new Exception("Число потоков не может быть отрицательным!");
            }
            M[][] res = calc.matrixSum(constRes, calc.scalarMultiplication(constRes, beta));
            return res;
        }
    }
}
