import ReadingType.IntegerRead;

import java.io.IOException;
import java.lang.reflect.Type;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        //For integer type
        Integer[][] matrixA = {
                {1,4},
                {2,3},
                {5,6}
        };
        Integer[][] matrixB = {
                {1,3,5},
                {2,4,6}
        };
        Integer alpha = 2;
        Integer beta = 3;
        Benchmark<Integer> calc = new Benchmark<>(Integer.class, matrixA, matrixB, alpha, beta);
        for (Integer[] row: calc.dgemm()) {
            System.out.println(Arrays.stream(row).toList());
        }

        System.out.println();
        //For BigInteger type
        BigInteger[][] bigIntMatrixA = {
                {BigInteger.valueOf(1), BigInteger.valueOf(4)},
                {BigInteger.valueOf(2), BigInteger.valueOf(3)},
                {BigInteger.valueOf(5), BigInteger.valueOf(6)}
        };
        BigInteger[][] bigIntMatrixB = {
                {BigInteger.valueOf(1), BigInteger.valueOf(3), BigInteger.valueOf(5)},
                {BigInteger.valueOf(2), BigInteger.valueOf(4), BigInteger.valueOf(6)}
        };
        BigInteger bigIntAlpha = BigInteger.valueOf(2);
        BigInteger bigIntBeta = BigInteger.valueOf(3);
        Benchmark<BigInteger> calc2 = new Benchmark<>(BigInteger.class, bigIntMatrixA, bigIntMatrixB, bigIntAlpha, bigIntBeta);
        for (BigInteger[] row: calc2.dgemm()) {
            System.out.println(Arrays.stream(row).toList());
        }

        System.out.println();
        //For Double type
        Double[][] dMatrixA = {
                {1.0, 4.0},
                {2.0, 3.0},
                {5.0, 6.0}
        };
        Double[][] dMatrixB = {
                {1.0, 3.0, 5.0},
                {2.0, 4.0, 6.0}
        };
        Double dAlpha = 2.0;
        Double dBeta = 3.0;
        Benchmark<Double> calc3 = new Benchmark<>(Double.class, dMatrixA, dMatrixB, dAlpha, dBeta);
        for (Double[] row: calc3.dgemm()) {
            System.out.println(Arrays.stream(row).toList());
        }
        LaunchBenchmarkJava test = new LaunchBenchmarkJava();
        IntegerRead intRead = new IntegerRead(test.fileRead());
        System.out.println(test.fileRead());
        for (Integer[] row: intRead.getMatrixA()) {
            System.out.println((Arrays.stream(row).toList()));
        }
        for (Integer[] row: intRead.getMatrixB()) {
            System.out.println((Arrays.stream(row).toList()));
        }
        for (Integer item: intRead.getScalars()) {
            System.out.println(item);
        }
    }
}