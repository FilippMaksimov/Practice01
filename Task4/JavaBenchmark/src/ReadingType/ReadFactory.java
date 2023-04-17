package ReadingType;

import BenchmarkCalculation.CalculationsFactory;

import java.math.BigInteger;
import java.util.List;

public class ReadFactory<T> {
    private Class<T> readClass;
    private List<String> input;
    public ReadFactory(Class<T> readClass, List<String> input) {
        this.readClass = readClass;
        this.input = input;
    }
    public DataRead<T> getSomeClass() {
        DataRead<T> data = null;
        if (readClass.equals(Integer.class)) {
            data = (DataRead<T>) new IntegerRead(input);
        }
        else if (readClass.equals(BigInteger.class)) {
            data = (DataRead<T>) new BigIntegerRead(input);
        }
        else if (readClass.equals(Double.class)) {
            data = (DataRead<T>) new DoubleRead(input);
        }
        return data;
    }
}
