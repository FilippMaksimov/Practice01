package ReadingType;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class BigIntegerRead implements DataRead<BigInteger> {
    private List<String> inputData;
    private int i;
    public BigIntegerRead(List<String> inputData) {
        this.inputData = inputData;
    }

    @Override
    public BigInteger[][] getMatrixA() {
        int rowA = Integer.parseInt(inputData.get(0));
        int columnA = Integer.parseInt(inputData.get(1));
        this.i = 2;
        BigInteger[][] matrixA = new BigInteger[rowA][columnA];
        for (int row = 0; row < rowA; row++) {
            for (int column = 0; column < columnA; column++) {
                if (inputData.get(i) != null) {
                    matrixA[row][column] = BigInteger.valueOf(Integer.parseInt(inputData.get(i)));
                    i++;
                }
                else break;
            }
        }
        i++;
        return matrixA;
    }

    @Override
    public BigInteger[][] getMatrixB() {
        int rowB = Integer.parseInt(inputData.get(i));
        i++;
        int columnB = Integer.parseInt(inputData.get(i));
        i++;
        BigInteger[][] matrixB = new BigInteger[rowB][columnB];
        for (int row = 0; row < rowB; row++) {
            for (int column = 0; column < columnB; column++) {
                if (inputData.get(i) != null) {
                    matrixB[row][column] = BigInteger.valueOf(Integer.parseInt(inputData.get(i)));
                    i++;
                }
                else break;
            }
        }
        i++;
        return matrixB;
    }

    @Override
    public BigInteger getAlpha() {
        return BigInteger.valueOf(Integer.parseInt(inputData.get(i)));
    }

    @Override
    public BigInteger getBeta() {
        i++;
        return BigInteger.valueOf(Integer.parseInt(inputData.get(i)));
    }
}
