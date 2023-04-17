import BenchmarkCalculation.CalculationsFactory;
import ReadingType.DataRead;
import ReadingType.ReadFactory;

import java.io.IOException;
import java.util.List;

public class BenchmarkLaunch<T> {
    private Class<T> someClass;
    private DataRead<T> data;
    public BenchmarkLaunch(Class<T> someClass) {
        this.someClass = someClass;
    }
    public void benchmarkStart() throws IOException {
        InputFileRead  dataList = new InputFileRead();
        DataRead<T> data = new ReadFactory<T>(someClass, dataList.fileRead()).getSomeClass();
        T[][] matrixA = data.getMatrixA();
        T[][] matrixB = data.getMatrixB();
        T alpha = data.getScalars().get(0);
        T beta = data.getScalars().get(1);
        Benchmark<T> bench = new Benchmark<T>(someClass, matrixA, matrixB, alpha, beta);
        long startTime = System.nanoTime();
        bench.dgemm();
    }
}
