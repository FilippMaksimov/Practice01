package BenchmarkCalculation;

public interface Calculations<M> {
    public abstract M[][] matrixTransposing(M[][] matrix);
    public abstract M[][] matrixMultiplication(M[][] matrixA, M[][] matrixB);
    public abstract M[][] scalarMultiplication(M[][] matrix, M scalar);
    public abstract M[][] matrixSum(M[][] matrixA, M[][] matrixB);
}
