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
    public M[][] dgemm() {
        Calculations<M> calc = new CalculationsFactory<M>(someClass).getSomeClass();
        M[][] transA = calc.matrixTransposing(matrixA);
        M[][] transB = calc.matrixTransposing(matrixB);
        M[][] constRes = calc.scalarMultiplication(calc.matrixMultiplication(transA, transB), alpha);
        M[][] res = calc.matrixSum(constRes, calc.scalarMultiplication(constRes, beta));
        return res;
    }
}
