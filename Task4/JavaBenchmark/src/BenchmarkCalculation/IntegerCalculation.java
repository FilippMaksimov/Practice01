package BenchmarkCalculation;

import BenchmarkCalculation.Calculations;
import org.w3c.dom.css.Counter;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;

public class IntegerCalculation implements Calculations<Integer> {
    @Override
    public Integer[][] matrixTransposing(Integer[][] matrix) {
        int rowsMatrix = matrix.length;
        int columnsMatrix = matrix[0].length;
        Integer[][] transposedMatrix = new Integer[columnsMatrix][rowsMatrix];
        for (int row = 0; row < rowsMatrix; row++) {
            for (int column = 0; column < columnsMatrix; column++) {
                transposedMatrix[column][row] = matrix[row][column];
            }
        }
        return transposedMatrix;
    }

    @Override
    public Integer[][] matrixMultiplication(Integer[][] matrixA, Integer[][] matrixB) {
        int rowsA = matrixA.length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        Integer[][] res = new Integer[rowsA][columnsB];
        for (int row = 0; row < rowsA; row++) {
            for (int column = 0; column < columnsB; column++) {
                res[row][column] = 0;
                for (int i = 0; i < rowsB; i++) {
                    res[row][column] += matrixA[row][i] * matrixB[i][column];
                }
            }
        }
        return res;
    }

    @Override
    public Integer[][] scalarMultiplication(Integer[][] matrix, Integer scalar) {
        int rowsMatrix = matrix.length;
        int columnsMatrix = matrix[0].length;
        for (int row = 0; row < rowsMatrix; row++) {
            for (int column = 0; column < columnsMatrix; column++) {
                matrix[row][column] *= scalar;
            }
        }
        return matrix;
    }

    @Override
    public Integer[][] matrixSum(Integer[][] matrixA, Integer[][] matrixB) {
        int rowsA = matrixA.length;
        int columnsA = matrixA[0].length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        if (rowsA == rowsB && columnsA == columnsB) {
            for (int row = 0; row < rowsA; row++) {
                for (int column = 0; column < columnsA; column++) {
                    matrixA[row][column] += matrixB[row][column];
                }
            }
        }
        return matrixA;
    }

    @Override
    public Integer[][] matrixMultiplicationThreads(Integer[][] matrixA, Integer[][] matrixB, int threads) throws InterruptedException {
        int rowsA = matrixA.length;
        int rowsB = matrixB.length;
        int columnsB = matrixB[0].length;
        Integer[][] res = new Integer[rowsA][columnsB];
        CountDownLatch latch = new CountDownLatch(rowsA);
        List<Thread> threadList = new ArrayList<>();
        for (int i = 0; i < threads; i++) {
            threadList.add(new Thread(() -> {
                synchronized (res) {
                    for (int row = 0; row < rowsA; row++) {
                        for (int column = 0; column < columnsB; column++) {
                            res[row][column] = 0;
                            for (int j = 0; j < rowsB; j++) {
                                res[row][column] += matrixA[row][j] * matrixB[j][column];
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
