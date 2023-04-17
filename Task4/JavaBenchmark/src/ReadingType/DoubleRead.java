package ReadingType;

import java.util.ArrayList;
import java.util.List;

public class DoubleRead implements DataRead<Double> {
    private List<String> inputData;
    private int i;
    public DoubleRead(List<String> inputData) {
        this.inputData = inputData;
    }

    @Override
    public Double[][] getMatrixA() {
        int rowA = Integer.parseInt(inputData.get(0));
        int columnA = Integer.parseInt(inputData.get(1));
        this.i = 2;
        Double[][] matrixA = new Double[rowA][columnA];
        for (int row = 0; row < rowA; row++) {
            for (int column = 0; column < columnA; column++) {
                if (inputData.get(i) != null) {
                    matrixA[row][column] = Double.valueOf(inputData.get(i));
                    i++;
                }
                else break;
            }
        }
        i++;
        return matrixA;
    }

    @Override
    public Double[][] getMatrixB() {
        int rowB = Integer.parseInt(inputData.get(i));
        i++;
        int columnB = Integer.parseInt(inputData.get(i));
        i++;
        Double[][] matrixB = new Double[rowB][columnB];
        for (int row = 0; row < rowB; row++) {
            for (int column = 0; column < columnB; column++) {
                if (inputData.get(i) != null) {
                    matrixB[row][column] = Double.valueOf(inputData.get(i));
                    i++;
                }
                else break;
            }
        }
        return matrixB;
    }

    @Override
    public List<Double> getScalars() {
        i++;
        List<Double> scalars = new ArrayList<>();
        Double alpha = Double.valueOf(inputData.get(i));
        i++;
        Double beta = Double.valueOf(inputData.get(i));
        scalars.add(0, alpha);
        scalars.add(1, beta);
        return scalars;
    }
}
