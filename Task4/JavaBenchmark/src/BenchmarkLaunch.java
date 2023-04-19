import ReadingType.DataRead;
import ReadingType.InputFileRead;
import ReadingType.ReadFactory;

import java.io.IOException;
import java.time.Instant;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class BenchmarkLaunch<T> {
    private Class<T> someClass;
    private int thread;
    public BenchmarkLaunch(Class<T> someClass, int thread) {

        this.someClass = someClass;
        this.thread = thread;
    }
    public List<Integer> benchmarkStart() throws IOException {
        InputFileRead dataList = new InputFileRead();
        DataRead<T> data = new ReadFactory<T>(someClass, dataList.fileRead()).getSomeClass();
        T[][] matrixA = data.getMatrixA();
        T[][] matrixB = data.getMatrixB();
        T alpha = data.getAlpha();
        T beta = data.getBeta();
        List<Integer> resList = new ArrayList<>();
        Benchmark<T> bench = new Benchmark<T>(someClass, matrixA, matrixB, alpha, beta);
        int diff = 0;
        for (int i=0; i != 10; i++) {
            LocalDateTime dStart = LocalDateTime.now();
            try {
                System.out.println(bench.dgemm(thread));
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
            LocalDateTime dEnd = LocalDateTime.now();
            diff += (dEnd.getNano() - dStart.getNano()) / 1000;
        }
        //Среднее время
        diff = diff / 10;
        int iMatrixA = matrixA.length * matrixA[0].length;
        int iMatrixB = matrixB.length * matrixB[0].length;
        int sum = iMatrixA + iMatrixB;
        resList.add(0, diff);
        resList.add(1, sum);
        return resList;
    }
}
