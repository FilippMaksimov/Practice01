package ReadingType;

import java.util.ArrayList;
import java.util.List;

public class IntegerRead implements DataRead<Integer> {
    private List<String> inputData;
    private int i;
    public IntegerRead(List<String> inputData) {
        this.inputData = inputData;
    }

    @Override
    public Integer[][] getMatrixA() {
        int rowA = Integer.parseInt(inputData.get(0));
        int columnA = Integer.parseInt(inputData.get(1));
        this.i = 2;
        Integer[][] matrixA = new Integer[rowA][columnA];
        for (int row = 0; row < rowA; row++) {
            for (int column = 0; column < columnA; column++) {
                if (inputData.get(i) != null) {
                    matrixA[row][column] = Integer.parseInt(inputData.get(i));
                    i++;
                }
                else break;
            }
        }
        i++;
        return matrixA;
    }

    @Override
    public Integer[][] getMatrixB() {
        int rowB = Integer.parseInt(inputData.get(i));
        i++;
        int columnB = Integer.parseInt(inputData.get(i));
        i++;
        Integer[][] matrixB = new Integer[rowB][columnB];
        for (int row = 0; row < rowB; row++) {
            for (int column = 0; column < columnB; column++) {
                if (inputData.get(i) != null) {
                    matrixB[row][column] = Integer.parseInt(inputData.get(i));
                    i++;
                }
                else break;
            }
        }
        i++;
        return matrixB;
    }

    @Override
    public Integer getAlpha() {
        return Integer.parseInt(inputData.get(i));
    }

    @Override
    public Integer getBeta() {
        i++;
        return Integer.parseInt(inputData.get(i));
    }
}
