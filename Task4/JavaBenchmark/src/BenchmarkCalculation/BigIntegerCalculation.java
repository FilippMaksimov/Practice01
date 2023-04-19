package BenchmarkCalculation;

import BenchmarkCalculation.Calculations;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;

public class BigIntegerCalculation implements Calculations<BigInteger> {
    @Override
    public BigInteger[][] matrixTransposing(BigInteger[][] matrix) {
        int rowsMatrix = matrix.length;
        int columnsMatrix = matrix[0].length;
        BigInteger[][] transposedMatrix = new BigInteger[columnsMatrix][rowsMatrix];
        for (int row = 0; row < rowsMatrix; row++)
        {
            for (int column = 0; column < columnsMatrix; column++)
            {
                transposedMatrix[column][row] = matrix[row][column];
            }
        }
        return transposedMatrix;
    }

    @Override
    public BigInteger[][] matrixMultiplication(BigInteger[][] matrixA, BigInteger[][] matrixB) {
        int rowsA = matrixA.length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        BigInteger[][] res = new BigInteger[rowsA][columnsB];
        for (int row = 0; row < rowsA; row++)
        {
            for (int column = 0; column < columnsB; column++)
            {
                res[row][column] = BigInteger.valueOf(0);
                for (int i = 0; i < rowsB; i++)
                {
                    res[row][column] = res[row][column].add(matrixA[row][i].multiply(matrixB[i][column]));
                }
            }
        }
        return res;
    }

    @Override
    public BigInteger[][] scalarMultiplication(BigInteger[][] matrix, BigInteger scalar) {
        int rowsMatrix = matrix.length;
        int columnsMatrix = matrix[0].length;
        for (int row = 0; row < rowsMatrix; row++)
        {
            for (int column = 0; column < columnsMatrix; column++)
            {
                matrix[row][column] = matrix[row][column].multiply(scalar);
            }
        }
        return matrix;
    }

    @Override
    public BigInteger[][] matrixSum(BigInteger[][] matrixA, BigInteger[][] matrixB) {
        int rowsA = matrixA.length;
        int columnsA = matrixA[0].length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        if (rowsA == rowsB && columnsA == columnsB)
        {
            for (int row = 0; row < rowsA; row++)
            {
                for (int column = 0; column < columnsA; column++)
                {
                    matrixA[row][column] = matrixA[row][column].add(matrixB[row][column]);
                }
            }
        }
        return matrixA;
    }

    @Override
    public BigInteger[][] matrixMultiplicationThreads(BigInteger[][] matrixA, BigInteger[][] matrixB, int threads)
            throws InterruptedException {
        int rowsA = matrixA.length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        BigInteger[][] res = new BigInteger[rowsA][columnsB];
        CountDownLatch latch = new CountDownLatch(rowsA);
        List<Thread> threadList = new ArrayList<>();
        for (int i = 0; i < threads; i++) {
            threadList.add(new Thread(() -> {
                synchronized (res) {
                    for (int row = 0; row < rowsA; row++) {
                        for (int column = 0; column < columnsB; column++) {
                            res[row][column] = BigInteger.valueOf(0);
                            for (int j = 0; j < rowsB; j++) {
                                res[row][column] = res[row][column].add(matrixA[row][j].multiply(matrixB[j][column]));
                            }
                        }
                    }
                }
                latch.countDown();
            }));
            threadList.get(i).start();
        }
        latch.await();
        return res;
    }
}
