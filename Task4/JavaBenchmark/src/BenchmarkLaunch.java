import ReadingType.DataRead;
import ReadingType.InputFileRead;
import ReadingType.ReadFactory;

import java.io.IOException;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

public class BenchmarkLaunch<T> {
    private Class<T> someClass;
    private int thread;
    public BenchmarkLaunch(Class<T> someClass, int thread) {

        this.someClass = someClass;
        this.thread = thread;
    }
    public List<Long> benchmarkStart() throws IOException {
        InputFileRead dataList = new InputFileRead();
        DataRead<T> data = new ReadFactory<T>(someClass, dataList.fileRead()).getSomeClass();
        T[][] matrixA = data.getMatrixA();
        T[][] matrixB = data.getMatrixB();
        T alpha = data.getAlpha();
        T beta = data.getBeta();
        List<Long> resList = new ArrayList<>();
        Benchmark<T> bench = new Benchmark<T>(someClass, matrixA, matrixB, alpha, beta);
        long operationTime = 0L;
        for (int i=0; i != 10; i++) {
            long startTime = Instant.now().toEpochMilli();
            //Добавить(реализовать) ниже в параметр число потоков!!
            bench.dgemm();
            long endTime = Instant.now().toEpochMilli();
            operationTime += (endTime - startTime);
        }
        //Среднее время
        operationTime = operationTime / 10;
        int iMatrixA = matrixA.length * matrixA[0].length;
        int iMatrixB = matrixB.length * matrixB[0].length;
        long sum = iMatrixA + iMatrixB;
        resList.add(0, operationTime);
        resList.add(1, sum);
        return resList;
    }
}
